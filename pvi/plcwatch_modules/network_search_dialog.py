import tkinter as tk
from typing import Union
from ipaddress import IPv4Network
import os
from pvi.Anslscan import ansl_scan, ScanResult
from pvi.plcwatch_modules.resources import icon_storage
from pvi.plcwatch_modules.ifaddr import get_adapters, IP as Ifaddr_IP

class NetworkSearchDialog:
    def __init__(self, parent : tk.Tk):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Search for CPUs")
        self.dialog.geometry("700x500")
        self.dialog.resizable(False, False)
        self.dialog.iconbitmap(icon_storage['app'])
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        left = parent.winfo_x()
        top = parent.winfo_y()   
        self.dialog.update_idletasks()
        x = left +  (parent.winfo_width() - self.dialog.winfo_width())//2
        y = top + (parent.winfo_height() - self.dialog.winfo_height())//2
        self.dialog.geometry(f'+{x}+{y}')
        
        # Create form
        main_frame = tk.Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
                
        
        # Create frame for listbox with network adapters
        tk.Label(main_frame, text="Available network adapters:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=10)        
        listbox_frame_adapters = tk.Frame(main_frame)
        listbox_frame_adapters.grid(row=1, column=0, pady=10, padx=0, sticky='ew')
        
        # Scrollbar
        scrollbar_adapters = tk.Scrollbar(listbox_frame_adapters)
        scrollbar_adapters.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for network adapters
        self.listbox_adapters = tk.Listbox(listbox_frame_adapters, font=('Arial', 10), 
                                           height=8, width=90, yscrollcommand=scrollbar_adapters.set, 
                                           selectmode=tk.SINGLE)
        self.listbox_adapters.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_adapters.config(command=self.listbox_adapters.yview)
        
        self.ip_addresses = []
        for adapter in get_adapters(include_unconfigured=True) :
            if adapter.operational_status == 'Up':
                for ip in adapter.ips:
                    if ip.is_IPv4:
                        self.ip_addresses.append(ip)
                        self.listbox_adapters.insert(tk.END, f"{ip.ip}/{ip.network_prefix} ({adapter.nice_name} / {ip.nice_name})")

        self.listbox_adapters.bind('<<ListboxSelect>>', self.adapter_selected )


        # Create frame for listbox for CPUs found
        self.result_cpu_found = tk.StringVar()
        self.result_cpu_found.set("0 CPU(s) found: (ANSL)")
        tk.Label(main_frame, textvariable= self.result_cpu_found, font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=10)
        listbox_frame_targets = tk.Frame(main_frame)
        listbox_frame_targets.grid(row=3, column=0, pady=10, padx=0, sticky='ew')
        
        # Scrollbar
        scrollbar_targets = tk.Scrollbar(listbox_frame_targets)
        scrollbar_targets.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for network adapters
        self.listbox_targets = tk.Listbox(listbox_frame_targets, font=('Arial', 10), 
                                height=8, width=90, yscrollcommand=scrollbar_targets.set, 
                                selectmode=tk.SINGLE)
        self.listbox_targets.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_targets.config(command=self.listbox_targets.yview)
        self.listbox_targets.bind('<<ListboxSelect>>', lambda e : self.button_ok.config( state = 'normal') )
        
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=4, column=0, pady=10)
        
        self.button_ok = tk.Button(button_frame, text="OK", command=self.ok_clicked, 
                                   width=10, font=('Arial', 10, 'bold'), state='disabled')
        self.button_ok.pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.cancel_clicked, 
                  width=10, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to OK
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())

        self.list_of_targets = []
        
                
    
    # an network adapter was select, we do a scan from it
    def adapter_selected(self, event : tk.Event ):
        if not self.listbox_adapters.curselection():
            return 'break' # why is this so complicated ?
        old_cursor = self.dialog.cget('cursor')
        self.dialog.config(cursor='watch')
        self.dialog.update_idletasks()
        self.button_ok.config( state = 'disabled')
        self.listbox_targets.delete(0,tk.END)        
        self.result_cpu_found.set("0 CPU(s) found: (ANSL)") 
        self.list_of_targets.clear()    
        try:        
            idx = self.listbox_adapters.curselection()[0]
            ifaddr_ip : Ifaddr_IP = self.ip_addresses[idx]
            network_prefix = max( min(ifaddr_ip.network_prefix,23), 24)
            ip = IPv4Network(f'{ifaddr_ip.ip}/{network_prefix}', strict=False)

            cpu_list = ansl_scan( IPv4Network(f'{ip.network_address}/{ip.prefixlen}'))
            self.result_cpu_found.set(f"{len(cpu_list)} CPU(s) found: (ANSL)")

            for cpu in cpu_list:
                cpu : ScanResult
                self.listbox_targets.insert(tk.END, f"CPU {cpu.target}, IP: {cpu.ip}, {cpu.AR}, {cpu.status}")    
                self.list_of_targets.append(cpu)
        except Exception as e:
            self.result_cpu_found.set("Error") 
        self.dialog.config(cursor=old_cursor) 
        return 'break'
                
     
    def ok_clicked(self):
        
        # Get selected CPU if any
        selected_cpu = None
        if self.listbox_targets.curselection():
            idx = self.listbox_targets.curselection()[0]
            target : ScanResult = self.list_of_targets[idx]
            self.result = target
            self.dialog.destroy()            

    
    def cancel_clicked(self):
        self.result = None
        self.dialog.destroy()
    
    def show(self) -> Union[ScanResult, None]:
        self.dialog.wait_window()
        return self.result

