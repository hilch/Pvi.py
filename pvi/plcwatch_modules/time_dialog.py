#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re
from pvi import Connection, Cpu
from .resources import icon_storage

class TimeDialog(tk.Toplevel):
    def __init__(self, parent: tk.Widget, pvi_connection : Connection, cpu : Cpu) -> None:
        super().__init__(parent)
        self.title("Set Date and Time")
        # Center the dialog
        left = parent.winfo_rootx()
        top = parent.winfo_rooty()   
        self.geometry(f'500x280+{left +50}+{top + 50}')   
        self.resizable(False, False)       
        self.iconbitmap(icon_storage['cpu'])        
        
        #self.transient(parent)
        self.grab_set()
        
        self.pvi_connection = pvi_connection
        self.cpu = cpu
        
        # Display current PC time
        self.pc_time_label: tk.Label = tk.Label(self, text="")
        self.pc_time_label.pack(pady=10)
        # Display current PLC time
        self.plc_time_label: tk.Label = tk.Label(self, text="")
        self.plc_time_label.pack(pady=10)        
        
        # Input fields
        tk.Label(self, text="Date (YYYY-MM-DD):").pack()
        self.date_entry: tk.Entry = tk.Entry(self, width=30)
        self.date_entry.pack(pady=5)
        
        tk.Label(self, text="Time (HH:MM:SS):").pack()
        self.time_entry: tk.Entry = tk.Entry(self, width=30)
        self.time_entry.pack(pady=5)
        
        # Display current time on load
        self.update_time()
        
        # Start automatic update every 10 seconds
        self.after_id: str = ""
        self.schedule_update()
        
        # Button frame
        button_frame: tk.Frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        btn_get: tk.Button = tk.Button(button_frame, text="Get PC time", command=self.get_pc_time, width=12)
        btn_get.grid(row=0, column=0, padx=5)
        
        btn_plc: tk.Button = tk.Button(button_frame, text="Get PLC time", command=self.get_plc_time, width=12)
        btn_plc.grid(row=0, column=1, padx=5)
        
        btn_set: tk.Button = tk.Button(button_frame, text="Set PLC time", command=self.set_plc_time, width=12)
        btn_set.grid(row=0, column=2, padx=5)
        
        btn_ok: tk.Button = tk.Button(button_frame, text="Ok", command=self.on_close, width=12)
        btn_ok.grid(row=0, column=3, padx=5)
        
        # Handle window close event
        self.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def schedule_update(self) -> None:
        """Schedule automatic update every second"""
        self.after_id = self.after(1000, self.auto_update)
    
    def auto_update(self) -> None:
        """Automatically update PC time every second"""
        self.update_time()
        self.schedule_update()
    
    def on_close(self) -> None:
        """Cancel scheduled update and close dialog"""
        if self.after_id:
            self.after_cancel(self.after_id)
        self.destroy()
    
    def update_time(self) -> datetime:
        current_time: datetime = datetime.now()
        time_str: str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.pc_time_label.config(text=f"Current PC time: {time_str}")
        
        plc_time = self.cpu.time
        time_str: str = plc_time.strftime("%Y-%m-%d %H:%M:%S")
        self.plc_time_label.config(text=f"Current PLC time: {time_str}")
          
        return current_time

    
    def validate_date(self, date_str: str) -> bool:
        pattern: str = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            return False
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    
    def validate_time(self, time_str: str) -> bool:
        pattern: str = r'^\d{2}:\d{2}:\d{2}$'
        if not re.match(pattern, time_str):
            return False
        try:
            datetime.strptime(time_str, "%H:%M:%S")
            return True
        except ValueError:
            return False
    
    
    def get_pc_time(self) -> None:
        current_time = self.update_time()
        
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, current_time.strftime("%Y-%m-%d"))
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, current_time.strftime("%H:%M:%S"))
   
    
    def get_plc_time(self) -> None:
        plc_time = self.cpu.time
        
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, plc_time.strftime("%Y-%m-%d"))
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, plc_time.strftime("%H:%M:%S"))
        
    
    def set_plc_time(self) -> None:
        date_str: str = self.date_entry.get()
        time_str: str = self.time_entry.get()
        
        if not self.validate_date(date_str):
            messagebox.showerror("Error", "Invalid date format!\nUse YYYY-MM-DD (e.g., 2026-03-26)")
            return
        
        if not self.validate_time(time_str):
            messagebox.showerror("Error", "Invalid time format!\nUse HH:MM:SS (e.g., 12:56:05)")
            return
        
        dt = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S')
        self.cpu.time = dt
        