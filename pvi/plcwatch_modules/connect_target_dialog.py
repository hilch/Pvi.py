import tkinter as tk
from tkinter import messagebox
import re
from pvi.plcwatch_modules.resources import icon_storage

class ConnectTargetDialog:
    def __init__(self, parent : tk.Tk):
        self.result = None
        self.dialog = tk.Toplevel(parent) if parent else tk.Tk()
        self.dialog.title("Connect to target")
        self.dialog.geometry("400x200")
        self.dialog.resizable(False, False)
        self.dialog.iconbitmap(icon_storage['app'])        
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (200 // 2)
        self.dialog.geometry(f"+{x}+{y}")
        
        # IP Address Label and Entry
        tk.Label(self.dialog, text="IP Address:", font=("Arial", 10)).grid(
            row=0, column=0, padx=20, pady=20, sticky="w"
        )
        self.ip_entry = tk.Entry(self.dialog, font=("Arial", 10), width=25)
        self.ip_entry.grid(row=0, column=1, padx=20, pady=20)
        self.ip_entry.insert(0, "192.168.1.1")  # Default value
        
        # Subnet Mask Label and Entry
        tk.Label(self.dialog, text="Subnet Mask:", font=("Arial", 10)).grid(
            row=1, column=0, padx=20, pady=20, sticky="w"
        )
        self.subnet_entry = tk.Entry(self.dialog, font=("Arial", 10), width=25)
        self.subnet_entry.grid(row=1, column=1, padx=20, pady=20)
        self.subnet_entry.insert(0, "255.255.255.0")  # Default value
        
        # Buttons Frame
        button_frame = tk.Frame(self.dialog)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        tk.Button(
            button_frame, text="OK", command=self.validate_and_close, 
            width=10, font=("Arial", 10)
        ).pack(side="left", padx=10)
        
        tk.Button(
            button_frame, text="Cancel", command=self.cancel, 
            width=10, font=("Arial", 10)
        ).pack(side="left", padx=10)
        
        # Bind Enter key to OK button
        self.dialog.bind("<Return>", lambda e: self.validate_and_close())
        self.dialog.bind("<Escape>", lambda e: self.cancel())
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
    def validate_ip(self, ip_string):
        """Validate IP address format and range"""
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        match = re.match(pattern, ip_string)
        
        if not match:
            return False
        
        # Check if all octets are in valid range (0-255)
        octets = [int(octet) for octet in match.groups()]
        return all(0 <= octet <= 255 for octet in octets)
    
    def validate_subnet(self, subnet_string):
        """Validate subnet mask format and validity"""
        if not self.validate_ip(subnet_string):
            return False
        
        # Convert subnet to binary and check if it's a valid mask
        octets = [int(octet) for octet in subnet_string.split('.')]
        binary = ''.join([format(octet, '08b') for octet in octets])
        
        # Valid subnet mask must be continuous 1s followed by continuous 0s
        # e.g., 11111111111111111111111100000000 is valid
        # but 11111111111111101111111100000000 is not valid
        stripped = binary.lstrip('1').lstrip('0')
        
        return len(stripped) == 0 and '1' in binary  # Must have at least one '1'
    
    def validate_and_close(self):
        """Validate both inputs and close dialog if valid"""
        ip_address = self.ip_entry.get().strip()
        subnet_mask = self.subnet_entry.get().strip()
        
        # Validate IP address
        if not self.validate_ip(ip_address):
            messagebox.showerror(
                "Invalid IP Address",
                "Please enter a valid IP address (e.g., 192.168.1.1).\n"
                "Each octet must be between 0 and 255."
            )
            self.ip_entry.focus()
            return
        
        # Validate subnet mask
        if not self.validate_subnet(subnet_mask):
            messagebox.showerror(
                "Invalid Subnet Mask",
                "Please enter a valid subnet mask (e.g., 255.255.255.0).\n"
                "The mask must be continuous 1s followed by 0s in binary."
            )
            self.subnet_entry.focus()
            return
        
        # If both are valid, store result and close
        self.result = {
            'ip_address': ip_address,
            'subnet_mask': subnet_mask
        }
        self.dialog.destroy()
    
    def cancel(self):
        """Cancel and close dialog"""
        self.result = None
        self.dialog.destroy()
    
    def show(self):
        """Show dialog and wait for result"""
        self.dialog.wait_window()
        return self.result