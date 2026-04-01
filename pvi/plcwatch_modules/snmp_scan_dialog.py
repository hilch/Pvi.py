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
from tkinter import ttk, messagebox
from typing import cast, List, Optional, Callable
import time
from dataclasses import dataclass
from pvi.plcwatch_modules.resources import icon_storage
from pvi import Connection, PviObject, Line, Device, Station, Variable, PviError

@dataclass
class SnmpScanResult:
    """Result of an SNMP scan"""
    target: str
    mac: str
    serialnumber: str
    ar_state: str
    ar_version: str
    ip_method: str
    ip_address: str
    subnet: str
    gateway: str

ar_state = {
    -1 : 'Unknown',
    1 : 'BOOT',
    2 : 'DIAG',
    3 : 'SERV',
    4 : 'RUN'
}

class SnmpScanDialog(tk.Toplevel):
    def __init__(self, parent: tk.Tk, pvi_connection : Connection):
        super().__init__(parent)
        # set size and position
        left = parent.winfo_rootx()
        top = parent.winfo_rooty()   
        self.geometry(f'1200x400+{left +50}+{top + 50}')   
        self.resizable(False, False)       
        self.iconbitmap(icon_storage['cpu'])             
        self.title("SNMP Scan Results")
        
        # Make dialog modal
        self.transient(parent)
        self.grab_set()
        
        # Create main frame
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        tk.Label(main_frame, text="SNMP Scan Results", font=('Arial', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        # Create treeview with columns
        columns = ('Target', 'MAC', 'Serialnumber', 'AR-State', 'AR-Version', 'IP-Mode', 'IP-Address', 'Subnet', 'Gateway')
        
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
            'Target': 120,
            'MAC': 120,
            'Serialnumber': 120,
            'AR-State': 100,
            'AR-Version': 100,
            'IP-Mode': 80,
            'IP-Address': 120,
            'Subnet': 120,
            'Gateway': 120
        }
        
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.W)
            self.tree.column(col, width=column_widths[col], anchor=tk.W)
        
        # Bind row selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_row_selected)
        
        # Bind double-click for editing
        self.tree.bind('<Double-Button-1>', self.onDoubleClick)
        
        # Store data for selected row
        self.scan_results: List[SnmpScanResult] = []
        
        # Editable columns
        self.editable_columns = ['IP-Mode', 'IP-Address', 'Subnet', 'Gateway']
        
        # Editor widgets
        # self.editor_widget: Optional[tk.Widget] = None
        # self.editing_item: Optional[str] = None
        # self.editing_column: Optional[str] = None
        
        # Button frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Refresh", command=self.refreshList, 
                 width=12, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)        
        
        tk.Button(button_frame, text="OK", command=self.onOK, 
                 width=12, font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        self.selected_index: int = -1
        self.result = '0.0.0.0'
        
        self.pvi_connection = pvi_connection
        self.line = Line( pvi_connection.root, 'LNSNMP', CD='LNSNMP')
        self.device = Device( self.line, 'Device', CD='/IF=snmp /RT=1000' )
        self.device.errorChanged =cast( Callable[[PviObject,int],None], self.deviceErrorChanged)    
    
    
    def deviceErrorChanged( self, device : Device, error : int ):     
        if error == 0:
            self.refreshList()
        else:
            pass  


    def clearAllEntries(self) -> None:
        """Clear all rows from the treeview"""
        # Delete all items from tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Clear scan_results list
        self.scan_results.clear()
        
        # Reset selection
        self.selected_index = -1
    
    
    def refreshList( self ):
        self.clearAllEntries()
        
        macs = [ x['name'] for x in self.device.externalObjects if x['type'] == 'Station']
        if len(macs) == 0:
            messagebox.showinfo('SNMP Scan', 'No Targets with SNMP activated found !')
        else:
            for mac in macs:
                self.update_idletasks()
                station = Station( self.device, 'station', CD=f'/CN={mac}' )
                
                values = dict()
                for name in ('targetTypeDescription',
                                'serialNumber',
                                'arState',
                                'arVersion',
                                'ipMethod',
                                'ipAddress',
                                'subnetMask',
                                'defaultGateway'
                                ) :
                    variable = Variable( station, name )
                    try:
                        values.update({ name : variable.value})
                    except PviError as e:
                        if e.number == 14787:
                            if variable.dataType == 'string':
                                values.update({ name : ''})
                            elif variable.dataType == 'i32':
                                values.update({ name : 0 })
                        else:
                            raise PviError(e.number)
                    variable.kill()

                station.kill()
                self.add_row( SnmpScanResult(
                    target = values['targetTypeDescription'],
                    mac = mac,
                    serialnumber=values['serialNumber'],
                    ar_state= ar_state.get( values['arState'], 'Unknown'),
                    ar_version=values['arVersion'],
                    ip_method= 'fixed IP' if values['ipMethod'] == 0 else 'DHCP',
                    ip_address=values['ipAddress'],
                    subnet=values['subnetMask'],
                    gateway=values['defaultGateway']
                    ))                           
  

    
    def onDoubleClick(self, event: tk.Event) -> None:
        """Handle double-click on tree item for editing"""
        region = self.tree.identify('region', event.x, event.y)
        if region != 'cell':
            return
        
        # Get column and item
        column = self.tree.identify_column(event.x)
        item = self.tree.identify_row(event.y)
        
        if not item or not column:
            return
        
        # Convert column ID to column name
        column_index = int(column.replace('#', '')) - 1
        if column_index < 0:
            return
        
        columns = self.tree['columns']
        if column_index >= len(columns):
            return
        
        column_name = columns[column_index]
        
        # Check if column is editable
        if column_name not in self.editable_columns:
            return
        
        # Get cell coordinates
        x, y, width, height = self.tree.bbox(item, column)
        
        
        # Get current value
        values = self.tree.item(item, 'values')
        current_value = values[column_index]
        current_mac = values[1]
        
        # Create editor based on column type
        if column_name == 'IP-Mode':
            self.createComboboxEditor(item, column_name, x, y, width, height, # type: ignore
                                        current_mac, current_value) 
        else:
            self.createEntryEditor(item, column_name, x, y, width, height, # type: ignore
                                     current_mac, current_value) 

    
    
    def createComboboxEditor(self, item: str, column: str, x: int, y: int, 
                               width: int, height: int, current_mac : str, current_value: str) -> None:
        """Create a combobox editor for IP-Mode column"""        
        # Create combobox
        combo = ttk.Combobox(self.tree, values=['DHCP', 'fixed IP'], state='readonly')
        combo.set(current_value)
        combo.place(x=x, y=y, width=width, height=height)
        combo.focus()

        def hideCombo(event: tk.Event) -> None:
            combo.destroy()
            self.tree.focus()
        
        def setIpMode(event: tk.Event) -> None:
            current_value = combo.get()
            station = Station( self.device, 'station', CD=f'/CN={current_mac}' )
            ip_address = Variable( station, 'ipAddress')            
            ip_method = Variable( station, 'ipMethod' )
            ip_method.value = 1 if current_value == 'DHCP' else 0
            ip_method.kill()
            combo.destroy()
            if current_value == 'DHCP':
                self.tree.config(cursor="watch")
                self.update_idletasks()  # Force cursor update
                start = time.time()
                while (time.time() - start) < 10:
                    if ip_address.value != ip_address:
                        break
            self.tree.config(cursor="")
            self.update_idletasks()  # Force cursor update                
            self.refreshList()
            ip_address.kill()
            station.kill()
            
        # Bind events
        combo.bind('<<ComboboxSelected>>', setIpMode)
        combo.bind('<FocusOut>', hideCombo)
        combo.bind('<Escape>', hideCombo)
          
    
    
    def createEntryEditor(self, item: str, column: str, x: int, y: int, 
                           width: int, height: int, current_mac : str, current_value: str) -> None:
        """Create an entry editor for IP-Address, Subnet, Gateway columns"""
        
        # Create entry
        entry = tk.Entry(self.tree)
        entry.insert(0, current_value)
        entry.select_range(0, tk.END)
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus()
        
        def hideEntry(event: tk.Event):
            entry.destroy()
            
        def saveEntry(event: tk.Event):
            current_value = entry.get()
            station = Station( self.device, 'station', CD=f'/CN={current_mac}' )
            variable = Variable( station, {'IP-Address' : 'ipAddress', 
                                           'Subnet' : 'subnetMask', 
                                           'Gateway' : 'defaultGateway'}[column] )
            try:
                variable.value = bytes(current_value,'ascii')
            except Exception as e:
                messagebox.showerror(f'Set {column}', f'Error setting {current_value} to {column}\n{e}')
            finally:
                variable.kill()
                station.kill()
                entry.destroy()
                self.refreshList()            
        
        # Bind events
        entry.bind('<Return>', saveEntry)
        entry.bind('<FocusOut>', hideEntry)
        entry.bind('<Escape>', hideEntry)
    
    
    def add_row(self, snmp_result: SnmpScanResult) -> None:
        """Add a row to the treeview"""
        values: tuple = (
            snmp_result.target,
            snmp_result.mac,
            snmp_result.serialnumber,
            snmp_result.ar_state,
            snmp_result.ar_version,
            snmp_result.ip_method,
            snmp_result.ip_address,
            snmp_result.subnet,
            snmp_result.gateway
        )
        
        # Insert row with index as first column
        row_index: int = len(self.scan_results) + 1
        self.tree.insert('', tk.END, text=str(row_index), values=values)
        self.scan_results.append(snmp_result)
    
    def on_row_selected(self, event: tk.Event) -> None:
        """Handle row selection"""
        selection: tuple = self.tree.selection()
        if selection:
            # Get the index of selected row
            item: str = selection[0]
            values = self.tree.item(item, 'values') 
            if isinstance(values, tuple):
                self.result = values[6] 
            else:
                self.result = '0.0.0.0'         
    
    def onOK(self) -> None:
        """Handle Cancel button click"""
        self.destroy()
    
    def show(self) -> str:
        """Show dialog and wait for result"""
        self.wait_window()
        return self.result