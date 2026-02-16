import tkinter as tk
from tkinter import messagebox
import re

class NetworkAddressDialog:
    def __init__(self, parent):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Network Address Configuration")
        self.dialog.geometry("400x200")
        self.dialog.resizable(False, False)
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (200 // 2)
        self.dialog.geometry(f'+{x}+{y}')
        
        # Create form
        main_frame = tk.Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # IP Address
        tk.Label(main_frame, text="IP Address:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=10)
        self.ip_entry = tk.Entry(main_frame, font=('Arial', 10), width=25)
        self.ip_entry.grid(row=0, column=1, pady=10, padx=10)
        self.ip_entry.insert(0, "192.168.1.1")
        
        # Subnet Mask
        tk.Label(main_frame, text="Subnet Mask:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=10)
        self.subnet_entry = tk.Entry(main_frame, font=('Arial', 10), width=25)
        self.subnet_entry.grid(row=1, column=1, pady=10, padx=10)
        self.subnet_entry.insert(0, "255.255.255.0")
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        tk.Button(button_frame, text="OK", command=self.ok_clicked, width=10, bg='#FF000F', fg='white', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.cancel_clicked, width=10, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Focus on IP entry
        self.ip_entry.focus()
        
        # Bind Enter key to OK
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())
        
    def validate_ip(self, ip):
        """Validate IP address format"""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if re.match(pattern, ip):
            parts = ip.split('.')
            return all(0 <= int(part) <= 255 for part in parts)
        return False
    
    def ok_clicked(self):
        ip = self.ip_entry.get().strip()
        subnet = self.subnet_entry.get().strip()
        
        # Validate inputs
        if not self.validate_ip(ip):
            messagebox.showerror("Invalid IP", "Please enter a valid IP address (e.g., 192.168.1.1)", parent=self.dialog)
            return
        
        if not self.validate_ip(subnet):
            messagebox.showerror("Invalid Subnet", "Please enter a valid subnet mask (e.g., 255.255.255.0)", parent=self.dialog)
            return
        
        self.result = {'ip': ip, 'subnet': subnet}
        self.dialog.destroy()
    
    def cancel_clicked(self):
        self.result = None
        self.dialog.destroy()
    
    def show(self):
        self.dialog.wait_window()
        return self.result