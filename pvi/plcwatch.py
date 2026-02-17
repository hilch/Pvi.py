import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

from pvi.plcwatch_modules import *
from pvi import *


class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.title("PLCWATCH")
        self.geometry("1024x768")
        self.iconbitmap(f'{script_dir}/plcwatch_modules/resources/app.ico')
        
        # Create menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Add File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Search for CPU", command=self.show_network_search_dialog)
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
        self.tree = ObjectTreeView(self.top_paned)
        
        # RIGHT SECTION: Multi-column Listbox (added directly to top_paned)
        # Create Treeview with columns for multi-column listbox
        self.listbox = VariableListBox(self.top_paned)

        # BOTTOM SECTION: Entry Widget directly in main_paned
        self.entry = tk.Entry(self.main_paned, font=('Arial', 12))
        self.main_paned.add(self.entry, minsize=30)
        self.entry.insert(0, "Type something here...")
        
        self.connection = Connection()
        self.line = Line( self.connection.root, 'LNANSL', CD='LNANSL')
        self.device = Device( self.line, 'TCP', CD='/IF=TcpIp' )
        self.after( 10, self.update)        
    
    def show_network_search_dialog(self):
        """Show the network search configuration dialog"""
        dialog = NetworkSearchDialog(self)
        result = dialog.show()
        
        if result:
            # Display the result in the entry field
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            
    def update(self):
        try:
            self.connection.doEvents() # execute PVI event loop
        except:
            pass
        self.after( 100, self.update)  

if __name__ == "__main__":
    app = ApplicationWindow()
    app.mainloop()
