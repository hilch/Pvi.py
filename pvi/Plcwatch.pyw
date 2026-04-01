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

from pathlib import Path
import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import threading
from typing import Union, List
from ipaddress import IPv4Address
from pvi.pvi_objects import Connection, PviObject, Line, Device, Cpu, Task, Variable
from pvi.plcwatch_modules import (NetworkSearchDialog, ScanResult, SnmpScanDialog,
                                VariableListBox, ObjectTreeView, icon_storage)
from pvi.__about__ import __version__



class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
              
        self.title("PLCWATCH")
        self.geometry("1024x768")
        self.iconbitmap(icon_storage['app'])
        
        self.app_configuration = dict()
        self.path_local_app_data =  Path(os.getenv('LOCALAPPDATA')) / 'Plcwatch'# type: ignore
        self.loadApplicationSettings()
                
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
        
        self.target_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Targets", menu=self.target_menu)
        self.target_menu.add_command(label="Search for Targets (ANSL)", command=self.showNetworkSearchDialog)    
        self.target_menu.add_separator()
        for n, ip in enumerate(self.app_configuration['ips']):
            self.target_menu.add_command(label=f"{n+1}. {ip}", command= lambda ip=ip : self.connectToIpAddress(ip) )
        self.target_menu.add_separator()
        self.target_menu.add_command(label="Search for Targets (SNMP)", command=self.showSnmpScanDialog)      
            
        self.help_menu = tk.Menu(menubar, tearoff=0) 
        menubar.add_cascade(label="Help", menu=self.help_menu) 
        self.help_menu.add_command(label="About", command=self.showAboutDialog)                 
                
        # Create main vertical PanedWindow (splits top and bottom)
        self.main_paned = tk.PanedWindow(self, orient=tk.VERTICAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Create horizontal PanedWindow for top section (splits left and right)
        self.top_paned = tk.PanedWindow(self.main_paned, orient=tk.HORIZONTAL, sashrelief=tk.FLAT, sashwidth=5)
        self.main_paned.add(self.top_paned, minsize=600)
        
        # LEFT SECTION: TreeView with Scrollbar
        # Create frame for treeview and scrollbar
        tree_frame = ttk.Frame(self.top_paned)
        
        # Create scrollbar
        tree_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create TreeView and link scrollbar
        self.tree = ObjectTreeView( parent=tree_frame, 
                                   yscrollcommand=tree_scrollbar.set,
                                   pvi_connection= self.pvi_connection, 
                                   callback_ip_connected = self.onConnectedToIpAddress,
                                   callback_mouse_leave= self.onTreeviewMouseLeave
                                   )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrollbar to control treeview
        tree_scrollbar.config(command=self.tree.yview)
        self.top_paned.add(tree_frame, minsize=300)
        
        # RIGHT SECTION: Multi-column Listbox (added directly to top_paned)
        # Create Treeview with columns for multi-column listbox
        listbox_frame = ttk.Frame(self.top_paned)
        # Create scrollbar
        listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create listbox and link scrollbar
        self.listbox = VariableListBox(parent = listbox_frame,
                                       yscrollcommand = listbox_scrollbar.set,
                                       pvi_connection= self.pvi_connection
                                       )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.top_paned.add(listbox_frame, minsize = 350)
        
               
        self.after( 10, self.update)        
        # thread = threading.Thread(target = self.pvi_cyclic)
        # thread.start()
    
    # def pvi_cyclic( self):
    #     pass
         
    def showAboutDialog(self):
        license = self.pvi_connection.license
        messagebox.showinfo( 'Plcwatch', f'https://github.com/hilch/Pvi.py\nVersion {__version__}'
                            f'\nSercurity mode: {license[0]}')
    
    def showNetworkSearchDialog(self):
        dialog = NetworkSearchDialog(self, self.pvi_connection, self.ansl_device)
        result : Union[ScanResult, None] = dialog.show()
        
        if result:
            self.tree.insertCpu( self.ansl_device, IPv4Address(result.ip) )
    
    def showSnmpScanDialog(self):
        dialog = SnmpScanDialog(self, self.pvi_connection)
        result = dialog.show()
        if result != '0.0.0.0':
            self.connectToIpAddress(result)
    
    def onTreeviewMouseLeave( self, object : PviObject ):
        self.listbox.announcePviObject( object )
       
            
    def onClosing(self):
        del self.pvi_connection
        self.destroy()
    
    def connectToIpAddress(self, ip : str ):
        self.tree.insertCpu( self.ansl_device, IPv4Address(ip))
    
    # after succesful connection to a cpu change menu 'Targets'
    def onConnectedToIpAddress(self, ip : str ):
        ips = self.app_configuration['ips']
        if ips[0] != ip:
            ips = ips[0:4]
            ips.insert(0,ip)
            for n, ip in enumerate(ips):
                self.target_menu.entryconfig(n+2, label = f"{n+1}. {ip}" )
            self.app_configuration['ips'] = ips  
            self.saveApplicationSettings()              
                       
                        
    def update(self):
        try:
            self.pvi_connection.doEvents() # execute PVI event loop
        except Exception as e:
            print(e)
        self.tree.update()
        self.after( 50, self.update)  


    def loadApplicationSettings(self):
        # Local AppData
        try:
            with open(self.path_local_app_data / 'config.json', 'r') as f:
                self.app_configuration = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            directory = Path(self.path_local_app_data)
            if not directory.exists():
                directory.mkdir()
            self.app_configuration = { 
                                      'ips' : ['127.0.0.1']*5
                                      }
            self.saveApplicationSettings()

            
    def saveApplicationSettings(self):
        try:
            with open(self.path_local_app_data / 'config.json', 'w') as f:
                json.dump(self.app_configuration, f)
        except Exception as e:
            pass
        

if __name__ == "__main__":
    app = ApplicationWindow()
    app.mainloop()
