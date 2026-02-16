import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

from pvi.plcwatch_modules import *
from pvi import *


class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.title("PLCWATCH")
        self.geometry("1024x768")
        
        # Create menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Add File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Search for CPU", command=self.show_network_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        # Create main vertical PanedWindow (splits top and bottom)
        self.main_paned = tk.PanedWindow(self, orient=tk.VERTICAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Create horizontal PanedWindow for top section (splits left and right)
        self.top_paned = tk.PanedWindow(self.main_paned, orient=tk.HORIZONTAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.add(self.top_paned, minsize=200)
        
        # LEFT SECTION: TreeView (added directly to top_paned)
        # Create TreeView with scrollbar
        tree_scroll = tk.Scrollbar(self.top_paned)
        
        self.tree = ttk.Treeview(self.top_paned, yscrollcommand=tree_scroll.set)
        self.top_paned.add(self.tree, minsize=150)
        
        tree_scroll.config(command=self.tree.yview)
        # Note: scrollbar added after tree to maintain proper z-order
        
        # Add sample data to TreeView
        self.tree.heading('#0', text='Tree View')
        parent1 = self.tree.insert('', 'end', text='Parent 1')
        self.tree.insert(parent1, 'end', text='Child 1.1')
        self.tree.insert(parent1, 'end', text='Child 1.2')
        parent2 = self.tree.insert('', 'end', text='Parent 2')
        self.tree.insert(parent2, 'end', text='Child 2.1')
        
        # RIGHT SECTION: Multi-column Listbox (added directly to top_paned)
        # Create Treeview with columns for multi-column listbox
        list_scroll = tk.Scrollbar(self.top_paned)
        
        # Define columns
        self.listbox = ttk.Treeview(self.top_paned, columns=('Name', 'Type', 'Value'), 
                                     show='headings', yscrollcommand=list_scroll.set)
        self.top_paned.add(self.listbox, minsize=150)
        
        list_scroll.config(command=self.listbox.yview)
        
        # Configure column headings
        self.listbox.heading('Name', text='Name')
        self.listbox.heading('Type', text='Type')
        self.listbox.heading('Value', text='Value')
        
        # Configure column widths
        self.listbox.column('Name', width=150, anchor='w')
        self.listbox.column('Type', width=100, anchor='center')
        self.listbox.column('Value', width=150, anchor='w')
        
        # Add sample data to multi-column listbox
        sample_data = [
            ('Variable_1', 'INT', '100'),
            ('Variable_2', 'BOOL', 'TRUE'),
            ('Variable_3', 'REAL', '3.14'),
            ('Temperature', 'REAL', '25.5'),
            ('Pressure', 'INT', '1013'),
            ('Status', 'BOOL', 'FALSE'),
            ('Counter', 'DINT', '12345'),
            ('Timer', 'TIME', '1000ms'),
            ('Speed', 'REAL', '45.8'),
            ('Position', 'INT', '500'),
            ('Alarm', 'BOOL', 'TRUE'),
            ('SetPoint', 'REAL', '100.0'),
            ('Output', 'INT', '75'),
            ('Input', 'INT', '50'),
            ('Mode', 'STRING', 'AUTO'),
        ]
        
        for item in sample_data:
            self.listbox.insert('', 'end', values=item)
        
        # BOTTOM SECTION: Entry Widget directly in main_paned
        self.entry = tk.Entry(self.main_paned, font=('Arial', 12))
        self.main_paned.add(self.entry, minsize=30)
        self.entry.insert(0, "Type something here...")
        
        self.connection = Connection()
        self.line = Line( self.connection.root, 'LNANSL', CD='LNANSL')
        self.device = Device( self.line, 'TCP', CD='/IF=TcpIp' )
        self.after( 10, self.update)        
    
    def show_network_dialog(self):
        """Show the network address configuration dialog"""
        dialog = NetworkAddressDialog(self)
        result = dialog.show()
        
        if result:
            # Display the result in the entry field
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"IP: {result['ip']} | Subnet: {result['subnet']}")
            
            # Add to multi-column listbox
            self.listbox.insert('', 'end', values=(f"Network_{result['ip']}", 'STRING', result['subnet']))
            
            print(f"Network configured: IP={result['ip']}, Subnet={result['subnet']}")

    def update(self):
        try:
            self.connection.doEvents() # execute PVI event loop
        except:
            pass
        self.after( 100, self.update)  

if __name__ == "__main__":
    app = ApplicationWindow()
    app.mainloop()
