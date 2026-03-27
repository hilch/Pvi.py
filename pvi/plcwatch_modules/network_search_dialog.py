import tkinter as tk
from typing import Union, List, Optional
from ipaddress import IPv4Network, IPv4Address
import asyncio
from dataclasses import dataclass
from pvi.plcwatch_modules.resources import icon_storage
from pvi.plcwatch_modules.ifaddr import get_adapters, IP as Ifaddr_IP

# Constants
ANSL_PORT = 11169
SOCKET_TIMEOUT = 1
MAX_CONCURRENT_SCANS = 256

@dataclass
class ScanResult:
    """Result of a network scan"""
    target: str
    ip: str
    AR: str = "Unknown"
    status: str = "Online"

class NetworkSearchDialog:
    def __init__(self, parent: tk.Tk):
        self.result: Optional[ScanResult] = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Search for CPUs")
        self.dialog.geometry("700x550")
        self.dialog.resizable(False, False)
        self.dialog.iconbitmap(icon_storage['app'])
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        left = parent.winfo_x()
        top = parent.winfo_y()   
        x = left + (parent.winfo_width() - self.dialog.winfo_width()) // 2
        y = top + (parent.winfo_height() - self.dialog.winfo_height()) // 2
        self.dialog.geometry(f'+{x}+{y}')
        
        # Create form
        main_frame = tk.Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Radio button variable to control selection mode
        self.selection_mode = tk.IntVar(value=1)  # 1 = adapter list, 2 = manual entry
        
        # Radio buttons frame
        radio_frame = tk.Frame(main_frame)
        radio_frame.grid(row=0, column=0, sticky='w', pady=5)
        
        tk.Radiobutton(radio_frame, text="Select from network adapters", 
                      variable=self.selection_mode, value=1, 
                      command=self.toggle_selection_mode,
                      font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(radio_frame, text="Enter network address manually", 
                      variable=self.selection_mode, value=2, 
                      command=self.toggle_selection_mode,
                      font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Create frame for listbox with network adapters
        tk.Label(main_frame, text="Available network adapters:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=10)        
        listbox_frame_adapters = tk.Frame(main_frame)
        listbox_frame_adapters.grid(row=2, column=0, pady=10, padx=0, sticky='ew')
        
        # Scrollbar
        scrollbar_adapters = tk.Scrollbar(listbox_frame_adapters)
        scrollbar_adapters.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for network adapters
        self.listbox_adapters = tk.Listbox(listbox_frame_adapters, font=('Arial', 10), 
                                           height=8, width=90, yscrollcommand=scrollbar_adapters.set, 
                                           selectmode=tk.SINGLE)
        self.listbox_adapters.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_adapters.config(command=self.listbox_adapters.yview)
        
        self.ip_addresses: List[Ifaddr_IP] = []
        for adapter in get_adapters(include_unconfigured=True):
            if adapter.operational_status == 'Up':
                for ip in adapter.ips:
                    if ip.is_IPv4:
                        self.ip_addresses.append(ip)
                        self.listbox_adapters.insert(tk.END, f"{ip.ip}/{ip.network_prefix} ({adapter.nice_name} / {ip.nice_name})")

        self.listbox_adapters.bind('<<ListboxSelect>>', self.adapter_selected)

        # Create frame for manual network address entry
        edit_frame = tk.Frame(main_frame)
        edit_frame.grid(row=3, column=0, pady=10, padx=0, sticky='ew')
        
        tk.Label(edit_frame, text="Network address (e.g., 192.168.1.0/24):", 
                font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 10))
        
        self.network_address = tk.StringVar()
        self.edit_network_address = tk.Entry(edit_frame, font=('Arial', 10), width=30, state='disabled', 
                                             textvariable=self.network_address)
        self.edit_network_address.pack(side=tk.LEFT, padx=5)
        
        # Scan button for manual entry
        self.button_scan = tk.Button(edit_frame, text="Scan", command=self.manual_scan_clicked, 
                                     width=10, font=('Arial', 10), state='disabled')
        self.button_scan.pack(side=tk.LEFT, padx=5)
        
        # Abort Scan button
        self.button_abort = tk.Button(edit_frame, text="Abort Scan", command=self.abort_scan_clicked, 
                                      width=10, font=('Arial', 10), state='disabled')
        self.button_abort.pack(side=tk.LEFT, padx=5)

        # Create frame for listbox for CPUs found
        self.result_cpu_found = tk.StringVar()
        self.result_cpu_found.set("0 CPU(s) found: (ANSL)")
        tk.Label(main_frame, textvariable=self.result_cpu_found, font=('Arial', 10)).grid(row=4, column=0, sticky='w', pady=10)
        listbox_frame_targets = tk.Frame(main_frame)
        listbox_frame_targets.grid(row=5, column=0, pady=10, padx=0, sticky='ew')
        
        # Scrollbar
        scrollbar_targets = tk.Scrollbar(listbox_frame_targets)
        scrollbar_targets.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for network adapters
        self.listbox_targets = tk.Listbox(listbox_frame_targets, font=('Arial', 10), 
                                height=8, width=90, yscrollcommand=scrollbar_targets.set, 
                                selectmode=tk.SINGLE)
        self.listbox_targets.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_targets.config(command=self.listbox_targets.yview)
        self.listbox_targets.bind('<<ListboxSelect>>', lambda e: self.button_ok.config(state='normal'))
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=6, column=0, pady=10)
        
        self.button_ok = tk.Button(button_frame, text="OK", command=self.ok_clicked, 
                                   width=10, font=('Arial', 10, 'bold'), state='disabled')
        self.button_ok.pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.cancel_clicked, 
                  width=10, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to OK
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())

        self.list_of_targets: List[ScanResult] = []
        
        # Scanning state
        self.scan_count: int = 0
        self.total_hosts: int = 0
        self.is_scanning: bool = False
        self.scan_aborted: bool = False
        self.scan_task: Optional[asyncio.Task] = None
    
    async def scan_host(self, ip: str) -> Optional[ScanResult]:
        """Scan a single host for ANSL port"""
        # Check if scan was aborted
        if self.scan_aborted:
            return None
            
        try:
            conn = asyncio.open_connection(ip, ANSL_PORT)
            reader, writer = await asyncio.wait_for(conn, timeout=SOCKET_TIMEOUT)
            writer.close()
            await writer.wait_closed()
            self.scan_count += 1
            return ScanResult(target=f"CPU@{ip}", ip=ip, AR="ANSL", status="Online")
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            self.scan_count += 1
            return None
    
    async def scan_network(self, network: IPv4Network) -> List[ScanResult]:
        """Scan network using asyncio with semaphore for concurrency control"""
        hosts = list(network.hosts())
        self.total_hosts = len(hosts)
        self.scan_count = 0
        results: List[ScanResult] = []
        
        # Create semaphore to limit concurrent scans
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_SCANS)
        
        async def scan_with_semaphore(ip: IPv4Address) -> Optional[ScanResult]:
            async with semaphore:
                return await self.scan_host(str(ip))
        
        # Create tasks for all hosts
        tasks = [scan_with_semaphore(ip) for ip in hosts]
        
        # Process results as they complete
        for coro in asyncio.as_completed(tasks):
            # Check if scan was aborted
            if self.scan_aborted:
                break
                
            result = await coro
            if result:
                results.append(result)
        
        return results
    
    def update_scan_progress(self):
        """Update scan progress every 5 seconds"""
        if self.is_scanning:
            self.result_cpu_found.set(f"Scanning: {self.scan_count}/{self.total_hosts} hosts checked...")
            self.dialog.after(5000, self.update_scan_progress)
    
    async def run_scan_async(self, network: IPv4Network) -> List[ScanResult]:
        """Run async scan with progress updates"""
        self.is_scanning = True
        self.scan_aborted = False
        self.scan_count = 0
        
        # Start progress updates
        self.update_scan_progress()
        
        try:
            cpu_list = await self.scan_network(network)
        finally:
            self.is_scanning = False
        
        return cpu_list
    
    def run_async_scan(self, network: IPv4Network):
        """Run async scan in a way that allows tkinter updates"""
        # Disable scan button, enable abort button
        self.button_scan.config(state='disabled')
        self.button_abort.config(state='normal')
        
        # Create new event loop in a thread-safe way
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # Schedule the scan task
            self.scan_task = loop.create_task(self.run_scan_async(network))
            
            # Run the loop step by step, allowing tkinter updates
            while not self.scan_task.done():
                loop.run_until_complete(asyncio.sleep(0.1))
                self.dialog.update()  # Allow tkinter to process events
            
            # Get the result
            cpu_list = self.scan_task.result()
            return cpu_list
        finally:
            loop.close()
            # Re-enable scan button, disable abort button
            if self.selection_mode.get() == 2:  # Only enable if in manual mode
                self.button_scan.config(state='normal')
            self.button_abort.config(state='disabled')
    
    def abort_scan_clicked(self):
        """Abort the current scan"""
        self.scan_aborted = True
        self.is_scanning = False
        self.result_cpu_found.set(f"Scan aborted! {self.scan_count}/{self.total_hosts} hosts checked.")
        self.button_abort.config(state='disabled')
        if self.selection_mode.get() == 2:
            self.button_scan.config(state='normal')
    
    def toggle_selection_mode(self):
        """Toggle between adapter list and manual entry mode"""
        if self.selection_mode.get() == 1:
            # Enable adapter listbox, disable manual entry
            self.listbox_adapters.config(state='normal')
            self.edit_network_address.config(state='disabled')
            self.button_scan.config(state='disabled')
            self.button_abort.config(state='disabled')
        else:
            # Disable adapter listbox, enable manual entry
            self.listbox_adapters.config(state='disabled')
            self.edit_network_address.config(state='normal')
            self.button_scan.config(state='normal')
            self.button_abort.config(state='disabled')
    
    def manual_scan_clicked(self):
        """Perform scan from manually entered network address"""
        network_addr = self.edit_network_address.get().strip()
        if not network_addr:
            return
        
        old_cursor = self.dialog.cget('cursor')
        self.dialog.config(cursor='watch')
        self.dialog.update_idletasks()
        self.button_ok.config(state='disabled')
        self.listbox_targets.delete(0, tk.END)
        self.result_cpu_found.set("0 CPU(s) found: (ANSL)")
        self.list_of_targets.clear()
        
        try:
            ip = IPv4Network(network_addr, strict=False)
            cpu_list = self.run_async_scan(ip)
            
            if self.scan_aborted:
                self.result_cpu_found.set(f"Scan aborted! Found {len(cpu_list)} CPU(s): (ANSL)")
            else:
                self.result_cpu_found.set(f"{len(cpu_list)} CPU(s) found: (ANSL)")
            
            for cpu in cpu_list:
                self.listbox_targets.insert(tk.END, f"CPU {cpu.target}, IP: {cpu.ip}, {cpu.AR}, {cpu.status}")
                self.list_of_targets.append(cpu)
        except Exception as e:
            self.result_cpu_found.set(f"Error: {str(e)}")
        
        self.dialog.config(cursor=old_cursor)
    
    def adapter_selected(self, event: tk.Event):
        """An network adapter was selected, we do a scan from it"""
        if not self.listbox_adapters.curselection():
            return 'break'
        
        old_cursor = self.dialog.cget('cursor')
        self.dialog.config(cursor='watch')
        self.dialog.update_idletasks()
        self.button_ok.config(state='disabled')
        self.listbox_targets.delete(0, tk.END)        
        self.result_cpu_found.set("0 CPU(s) found: (ANSL)") 
        self.list_of_targets.clear()    
        
        # Enable abort button during adapter scan
        self.button_abort.config(state='normal')
        
        try:        
            idx = self.listbox_adapters.curselection()[0]
            ifaddr_ip: Ifaddr_IP = self.ip_addresses[idx]
            network_prefix = max(min(ifaddr_ip.network_prefix, 23), 24)
            ip = IPv4Network(f'{ifaddr_ip.ip}/{network_prefix}', strict=False)
            self.network_address.set(ip.compressed)  # preset the field for manual scan
            cpu_list = self.run_async_scan(IPv4Network(f'{ip.network_address}/{ip.prefixlen}'))
            
            if self.scan_aborted:
                self.result_cpu_found.set(f"Scan aborted! Found {len(cpu_list)} CPU(s): (ANSL)")
            else:
                self.result_cpu_found.set(f"{len(cpu_list)} CPU(s) found: (ANSL)")

            for cpu in cpu_list:
                self.listbox_targets.insert(tk.END, f"CPU {cpu.target}, IP: {cpu.ip}, {cpu.AR}, {cpu.status}")    
                self.list_of_targets.append(cpu)
        except Exception as e:
            self.result_cpu_found.set(f"Error: {str(e)}") 
        
        self.dialog.config(cursor=old_cursor)
        self.button_abort.config(state='disabled')
        return 'break'
                
    def ok_clicked(self):
        """Handle OK button click"""
        # Get selected CPU if any
        if self.listbox_targets.curselection():
            idx = self.listbox_targets.curselection()[0]
            target: ScanResult = self.list_of_targets[idx]
            self.result = target
            self.dialog.destroy()            

    def cancel_clicked(self):
        """Handle Cancel button click"""
        self.result = None
        self.dialog.destroy()
    
    def show(self) -> Optional[ScanResult]:
        """Show dialog and wait for result"""
        self.dialog.wait_window()
        return self.result