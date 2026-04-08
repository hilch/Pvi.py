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
from tkinter import ttk
from typing import List, Optional
from dataclasses import dataclass
from pvi.plcwatch_modules.resources import icon_storage
from pvi.pvi_objects import Connection, PviObject, Cpu, Module

@dataclass
class ModuleInfo:
    """Information about a module"""
    name: str
    type: str
    size: str
    timestamp: str
    version: str

class ListModulesDialog(tk.Toplevel):
    def __init__(self, parent: tk.Widget, pvi_connection : Connection , cpu : Cpu):
        super().__init__(parent)
        self.title("List Modules")
        # Center the dialog
        left = parent.winfo_rootx()
        top = parent.winfo_rooty()   
        self.geometry(f'800x400+{left +50}+{top + 50}')              
        self.resizable(False, False)
        self.iconbitmap(icon_storage['cpu'])
        
        # Make dialog modal
        # self.transient(parent)
        self.grab_set()
        
        # Create main frame
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        tk.Label(main_frame, text="Modules", font=('Arial', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        # Create treeview with columns
        columns = ('Name', 'Type', 'Size', 'Timestamp', 'Version')
        
        # Create frame for treeview and scrollbar
        tree_frame = tk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Vertical scrollbar
        scrollbar_v = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Horizontal scrollbar
        scrollbar_h = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Create Treeview
        self.tree: ttk.Treeview = ttk.Treeview(tree_frame, 
                                columns=columns, 
                                height=10,
                                yscrollcommand=scrollbar_v.set,
                                xscrollcommand=scrollbar_h.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrollbars
        scrollbar_v.config(command=self.tree.yview)
        scrollbar_h.config(command=self.tree.xview)
        
        # Define column headings and widths
        self.tree.heading('#0', text='#', anchor=tk.W)
        self.tree.column('#0', width=40, anchor=tk.W)
        
        column_widths: dict = {
            'Name': 200,
            'Type': 150,
            'Size': 100,
            'Timestamp': 120,
            'Version': 120
        }
        
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.W)
            self.tree.column(col, width=column_widths[col], anchor=tk.W)
        
        # Bind row selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_row_selected)
        
        # Store data for selected row
        self.modules: List[ModuleInfo] = []
        
        # Button frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # self.button_ok: tk.Button = tk.Button(button_frame, text="OK", command=self.ok_clicked, 
        #                            width=12, font=('Arial', 10), state='disabled')
        # self.button_ok.pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="OK", command=self.cancel_clicked, 
                 width=12, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter and Escape keys
        self.bind('<Return>', lambda e: self.ok_clicked())
        self.bind('<Escape>', lambda e: self.cancel_clicked())
        
        self.selected_index: int = -1
        self.result: Optional[ModuleInfo] = None
        
        self.pvi_connection = pvi_connection
        self.cpu = cpu
        
        modules = cpu.modules
        
        for name in modules:
            module = Module( cpu, name.replace('::','__'),  CD=f'"{name}"' )
            module_info = module.moduleInfoExtended
            self.add_module( ModuleInfo(
                name=name, 
                type=module_info['ModulType'], 
                size=module_info['Size'], 
                timestamp=module_info['Time'], 
                version=module_info['Version'])
                )
            module.kill()
    
    
    def add_module(self, module_info: ModuleInfo) -> None:
        """Add a module to the treeview"""
        values: tuple = (
            module_info.name,
            module_info.type,
            module_info.size,
            module_info.timestamp,
            module_info.version
        )
        
        # Insert row with index as first column
        row_index: int = len(self.modules) + 1
        self.tree.insert('', tk.END, text=str(row_index), values=values)
        self.modules.append(module_info)
    
    def on_row_selected(self, event: tk.Event) -> None:
        """Handle row selection"""
        selection: tuple = self.tree.selection()
        if selection:
            # self.button_ok.config(state='normal')
            # Get the index of selected row
            item: str = selection[0]
            self.selected_index: int = self.tree.index(item)
    
    def ok_clicked(self) -> None:
        """Handle OK button click"""
        if 0 <= self.selected_index < len(self.modules):
            self.result = self.modules[self.selected_index]
            self.destroy()
    
    def cancel_clicked(self) -> None:
        """Handle Cancel button click"""
        self.result = None
        self.destroy()
    
    def show(self) -> Optional[ModuleInfo]:
        """Show dialog and wait for result"""
        self.wait_window()
        return self.result
