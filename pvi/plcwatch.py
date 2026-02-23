import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import threading
from typing import Union, List
from ipaddress import IPv4Address
from pvi import Connection, Line, Device
from pvi.plcwatch_modules import (NetworkSearchDialog, ConnectTargetDialog, 
                                VariableListBox, ObjectTreeView, icon_storage)
from pvi.Anslscan import ScanResult



class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.title("PLCWATCH")
        self.geometry("1024x768")
        self.iconbitmap(icon_storage['app'])
        
        # create PVI objects
        self.pvi_connection = Connection()
        self.ansl_line = Line( self.pvi_connection.root, 'LNANSL', CD='LNANSL')
        self.ansl_device = Device( self.ansl_line, 'TCP', CD='/IF=TcpIp' )        
        
        # Create menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Add File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)
        
        target_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Targets", menu=target_menu)
        target_menu.add_command(label="Search for Targets", command=self.show_network_search_dialog)
        target_menu.add_command(label="Connect to Target", command=self.show_connect_target_dialog)        
        #file_menu.add_separator()
        
        # Create main vertical PanedWindow (splits top and bottom)
        self.main_paned = tk.PanedWindow(self, orient=tk.VERTICAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Create horizontal PanedWindow for top section (splits left and right)
        self.top_paned = tk.PanedWindow(self.main_paned, orient=tk.HORIZONTAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.add(self.top_paned, minsize=200)
        
        # LEFT SECTION: TreeView (added directly to top_paned)
        # Create TreeView with scrollbar
        self.tree = ObjectTreeView(self, self.pvi_connection)
        self.top_paned.add(self.tree, minsize=150)
        
        # RIGHT SECTION: Multi-column Listbox (added directly to top_paned)
        # Create Treeview with columns for multi-column listbox
        self.listbox = VariableListBox(self.top_paned)

        # BOTTOM SECTION: Entry Widget directly in main_paned
        self.entry = tk.Entry(self.main_paned, font=('Arial', 12))
        self.main_paned.add(self.entry, minsize=30)
        self.entry.insert(0, "Type something here...")
               
        self.after( 10, self.update)        
        thread = threading.Thread(target = self.pvi_cyclic)
        thread.start()
    
    def pvi_cyclic( self):
        pass
       
    def show_network_search_dialog(self):
        dialog = NetworkSearchDialog(self)
        result : Union[ScanResult, None] = dialog.show()
        
        if result:
            self.tree.insert_cpu( self.ansl_device, IPv4Address(result.ip))
            # Display the result in the entry field
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
    
            
    def show_connect_target_dialog(self):
        dialog = ConnectTargetDialog(self)
        result = dialog.show()
                    
            
    def update(self):
        try:
            self.pvi_connection.doEvents() # execute PVI event loop
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(e) ) 
        self.after( 100, self.update)  

if __name__ == "__main__":
    app = ApplicationWindow()
    app.mainloop()
