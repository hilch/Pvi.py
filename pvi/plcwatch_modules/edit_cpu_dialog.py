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
import ipaddress
import time
from typing import cast, Callable
from pvi.pvi_objects import Connection, Line, PviObject, Device, Station, Cpu, Task, Variable, PviError
from .resources import icon_storage


def validateIpv4(ip_string):
    """
    Validate if a string is a valid IPv4 address.
    
    Args:
        ip_string (str): The IP address string to validate
        
    Returns:
        bool: True if valid IPv4 address, False otherwise
    """
    try:
        ipaddress.IPv4Address(ip_string)
        return True
    except ValueError:
        return False


class EditCpuDialog( tk.Toplevel):
    def __init__(self, parent : tk.Widget, pvi_connection : Connection, cpu : Cpu ):
        super().__init__(parent)
        self.title("Edit CPU")
        # set size and position
        left = parent.winfo_rootx()
        top = parent.winfo_rooty()   
        self.geometry(f'400x450+{left +50}+{top + 50}')      
        self.resizable(False, False)       
        self.iconbitmap(icon_storage['cpu'])
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) 
        self.protocol("WM_DELETE_WINDOW", self.onCancelClicked)  # Intercept close button       
        
        self.pvi_connection = pvi_connection
        
        self.cpu = cpu
        cpu_info_extended = cpu.cpuInfoExtended
        self.ip_address = self.cpu.objectName.replace('_','.')
        self.mac_address = None
        
        # Variables
        self.ip_method_alternatives = { 0 : 'fixed IP', 1 : 'DHCP-Client'}        
        self.ip_method_var = tk.StringVar( value='DHCP-Client')
        self.ina_activated_var = tk.BooleanVar()  
        self.network_settings_changed = False
        
        # Styles
        self.style_entry_invalid_content = ttk.Style()
        self.style_entry_invalid_content.configure('Invalid.TEntry', foreground='red')                
        
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        
        # ===== Display Labels Section =====
        row = 0
        ttk.Label(main_frame, text="System Information", font=("Arial", 10, "bold")).grid(row=row, column=0, pady=(0, 10), sticky="w")
        
        row+=1
        ttk.Label(main_frame, text="CPU:").grid(row=row, column=0, sticky="w")
        self.cpu_label = ttk.Label(main_frame, 
                                   text=cpu_info_extended['CpuConfiguration']['Type']+' / ' + cpu_info_extended['CpuConfiguration']['ShortName'], 
                                   relief="sunken")
        self.cpu_label.grid(row=row, column=1, sticky="ew", padx=5 )
        
        row+=1
        ttk.Label(main_frame, text="MAC:").grid(row=row, column=0, sticky="w")
        self.mac_label = ttk.Label(main_frame, text="?", relief="sunken")
        self.mac_label.grid(row=row, column=1, sticky="ew", padx=5 )
        
        row+=1
        ttk.Label(main_frame, text="Serialnumber:").grid(row=row, column=0, sticky="w")
        self.serial_number = ttk.Label(main_frame, text="?", relief="sunken")
        self.serial_number.grid(row=row, column=1, sticky="ew", padx=5 )        
        
        row+=1
        ttk.Label(main_frame, text="AR-State:").grid(row=row, column=0, sticky="w")
        self.ar_state_label = ttk.Label(main_frame, 
                                        text=cpu_info_extended['OperationalValues']['CurrentCpuMode'], 
                                        relief="sunken")
        self.ar_state_label.grid(row=row, column=1, sticky="ew", padx=5)
        
        row+=1
        ttk.Label(main_frame, text="AR-Version:").grid(row=row, column=0, sticky="w")
        self.ar_version_label = ttk.Label(main_frame, 
                                        text=cpu_info_extended['SoftwareVers']['AutomationRuntime'], 
                                        relief="sunken")
        self.ar_version_label.grid(row=row, column=1, sticky="ew", padx=5 )    
        
        row+=1        
        ttk.Label(main_frame, text="Hardware Node Number").grid(row=row, column=0, sticky="w")
        self.node_number_label = ttk.Label(main_frame, text='?', relief="sunken")
        self.node_number_label.grid(row=row, column=1, sticky="ew", padx=5 )                   
        
        row+=1        
        ttk.Label(main_frame, text="SNMP-Mode").grid(row=row, column=0, sticky="w")
        self.snmpmode_label = ttk.Label(main_frame, text="deactivated", relief="sunken")
        self.snmpmode_label.grid(row=row, column=1, sticky="ew", padx=5 )               
        
        # ===== Network Settings =====
        row+=1
        ttk.Label(main_frame, text='Network Settings', font=('Arial', 10, "bold")).grid(row=row, column=0, pady=(15, 10), sticky="w")

        row+=1
        ttk.Label(main_frame, text='IP-Mode').grid(row=row, column=0, sticky="w")
        self.ip_method_combo = ttk.Combobox( main_frame, textvariable = self.ip_method_var,
                                            values=list(self.ip_method_alternatives.values()), 
                                            state ='readonly' )
        self.ip_method_combo.bind( '<<ComboboxSelected>>', self.onIpMethodChanged )
        self.ip_method_combo.grid(row=row, column=1, sticky="w")  
    
        
        row+=1
        ttk.Label(main_frame, text='IP:').grid(row=row, column=0, sticky="w")
        self.ip_entry = ttk.Entry(main_frame)
        self.ip_entry.bind ('<KeyRelease>', self.onNetworkSettingsChanged )        
        self.ip_entry.insert(0, self.ip_address)
        self.ip_entry.grid(row=row, column=1, sticky="ew" )

        row+=1       
        ttk.Label(main_frame, text='SUBNET:').grid(row=row, column=0, sticky="w")
        self.subnet_entry = ttk.Entry(main_frame)
        self.subnet_entry.bind ('<KeyRelease>', self.onNetworkSettingsChanged )        
        self.subnet_entry.insert(0, '?')
        self.subnet_entry.grid(row=row, column=1, sticky="ew")
        
        row+=1
        ttk.Label(main_frame, text="GATEWAY:").grid(row=row, column=0, sticky="w")
        self.gateway_entry = ttk.Entry(main_frame)
        self.gateway_entry.bind ('<KeyRelease>', self.onNetworkSettingsChanged )                
        self.gateway_entry.insert(0, "?")
        self.gateway_entry.grid(row=row, column=1, sticky="ew")
        
        row+=1
        self.log_label = ttk.Label(main_frame, text='read SNMP settings from CPU ...', relief=tk.SUNKEN)
        self.log_label.grid(row=row, column=0, columnspan=2, sticky="ew")
                      
        
        # ===== INA =====
        row+=1
        ttk.Label(main_frame, text='INA 2000 protocol', font=('Arial', 10, "bold")).grid(row=row, column=0, pady=(15, 10), sticky="w")      
        
        row+=1
        self.snmp_check = ttk.Checkbutton(main_frame, text="INA activated", variable=self.ina_activated_var, state='disabled')
        self.snmp_check.grid(row=row, column=0, columnspan=2, sticky="w")
                
        row+=1
        ttk.Label(main_frame, text="INA Node Number").grid(row=row, column=0, sticky="w")
        self.ina_node_number_label = ttk.Label(main_frame, text='?', relief="sunken")
        self.ina_node_number_label.grid(row=row, column=1, sticky="ew", padx=5 )         

        # ==== Options ====
        # row+=1
        # ttk.Label(main_frame, text="Options", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=2, pady=(15, 10), sticky="w")
            
        # row+=1        
        # ttk.Label(main_frame, text="SNMP-Mode").grid(row=row, column=0, sticky="w")
        # # self.snmpmode_label = ttk.Label(main_frame, text="deactivated")
        # # self.snmpmode_label.grid(row=row, column=1, sticky="ew", padx=5 )       
        

        
        # ===== Buttons =====
        row+=1
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=(15, 0), sticky="ew")
        
        self.ok_button = ttk.Button(button_frame, text="OK", state='disabled', command=self.onOkClicked)
        self.ok_button.pack(side="left", padx=5)
        
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.onCancelClicked)
        cancel_button.pack(side="left", padx=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        
        self.grab_set()
        self.result = None
        self.line = Line( pvi_connection.root, 'LNSNMP', CD='LNSNMP')
        self.device = Device( self.line, 'Device', CD='/IF=snmp /RT=1000' )
        self.device.errorChanged =cast( Callable[[PviObject,int],None], self.deviceErrorChanged)
        self.setWidgetStateNetworkSettings(False)
    
    def logInfo( self, text : str ):
        self.log_label.config( text = text)
    

    def onNetworkSettingsChanged( self, event ):
        self.network_settings_changed = True
        ip_address = self.ip_entry.get()
        valid = True
        if not validateIpv4( ip_address ):
            self.ip_entry.configure(style='Invalid.TEntry')
            valid = False
        else:
            self.ip_entry.configure(style='TEntry')
            
        subnet_mask = self.subnet_entry.get()
        if not validateIpv4( subnet_mask ):
            self.subnet_entry.configure(style='Invalid.TEntry')
            valid = False            
        else:
            self.subnet_entry.configure(style='TEntry')       
            
        gateway = self.gateway_entry.get()
        if not validateIpv4( gateway ):
            self.gateway_entry.configure(style='Invalid.TEntry')
            valid = False            
        else:
            self.gateway_entry.configure(style='TEntry')      

        if valid:
            self.ok_button.config( state='normal')            
        else:
            self.ok_button.config( state='disabled')
    
            
    def deviceErrorChanged( self, device : Device, error : int ):     
        if error == 0:
            for c in (self.ip_method_combo, self.ip_entry, self.subnet_entry, self.gateway_entry):
                    c.state(['disabled'])            
            
            macs = [ x['name'] for x in device.externalObjects if x['type'] == 'Station']
            if len(macs) == 0:
                pass
            else:
                for mac in macs:
                    self.update_idletasks()
                    station = Station( device, 'station', CD=f'/CN={mac}' )
                    ip_address = Variable( station, 'ipAddress')
                    if ip_address.value == bytes(self.ip_address,'ascii'):
                        self.mac_label.config( text = mac )
                        self.mac_address = mac
                        self.refreshWidgets(station)
                    ip_address.kill()
                    station.kill()
            self.log_label.config( text = '')
        else:
            pass


    
    def refreshWidgets(self, station : Station ):
        self.logInfo('read SNMP settings from CPU ...')        
        self.update_idletasks()  # Force cursor update        
        
        values = dict()
        for object in station.externalObjects:
            self.update_idletasks()  # Force cursor update   
            variable = Variable( station, object['name'] )
            try:
                value = variable.value
                values.update( { object['name'] : value })  
            except PviError as e:
                if e.number == 14787:
                    if variable.dataType == 'string':
                        values.update({ object['name'] : ''})
                    elif variable.dataType == 'i32':
                        values.update({ object['name'] : 0 })
                else:
                    raise PviError(e.number)
            finally:
                variable.kill()
                            
        self.serial_number.config( text = values['serialNumber'] )
        
        ip_method = values['ipMethod']
        self.ip_method_var.set( self.ip_method_alternatives[ip_method] )

        self.subnet_entry.delete(0,'end')
        self.subnet_entry.insert(0, values['subnetMask'] )
        
        self.gateway_entry.delete(0,'end')
        self.gateway_entry.insert(0, values['defaultGateway'] )
        
        snmp_mode = values['snmpMode']
        self.snmpmode_label.config( text = { 0 : 'deactivated', 1 : 'read-only', 2 : 'activated'}.
                                    get( snmp_mode , '?'))
        
        if 'nodeNumber' in values:
            self.node_number_label.config( text = values['nodeNumber'])
        self.ina_activated_var.set( values['inaActivated'])    
        
        if values['ipMethod'] == 0 and values['snmpMode'] != 0:
            self.setWidgetStateNetworkSettings(True)
        else:
            self.setWidgetStateNetworkSettings(False)
            
        if values['snmpMode'] != 2:
            self.ip_method_combo.config( state = 'deactivated')
        else:
            self.ip_method_combo.config( state = 'readonly')
    
        self.logInfo('')  
        self.config(cursor="")
        self.update_idletasks()
    
    
    def setWidgetStateNetworkSettings(self, activated : bool ):
        for c in (self.ip_entry,self.subnet_entry,self.gateway_entry):
            c.config( state = 'normal' if activated else 'readonly')  
    

    def onChangeNetworkSettings(self ):
        
        self.logInfo( 'change network settings.')        
        
        ip_address = self.ip_entry.get()      
        subnet_mask = self.subnet_entry.get()    
        gateway = self.gateway_entry.get() 
      
        try:
            station = Station( self.device, 'station', CD=f'/CN={self.mac_address}' )
            
            var_ip_method = Variable( station, 'ipMethod')
            var_ip_method.value = 0 # fixed IP            
            
            var_ip_address = Variable( station, 'ipAddress')
            var_ip_address.value = bytes(ip_address,'ascii')
            self.ip_address_changed = ip_address
            
            var_subnet_mask = Variable( station, 'subnetMask')                        
            var_subnet_mask.value = bytes(subnet_mask,'ascii')
            
            var_gateway = Variable( station, 'defaultGateway')
            var_gateway.value = bytes(gateway,'ascii')
        
        except PviError as e:
            self.logInfo( f'PviError: {e.number}' ) 

        finally: 
            try:       
                var_ip_address.kill()
                var_subnet_mask.kill()
                var_gateway.kill()
            except:
                pass
        station.kill()
     
        
    def onIpMethodChanged(self, event ): 
        self.setWidgetStateNetworkSettings(False) 
        self.network_settings_changed = True       
        methods = { v : k for k, v in self.ip_method_alternatives.items() }
        intended_ip_method = methods[self.ip_method_var.get()]
        
        try:
            station = Station( self.device, 'station', CD=f'/CN={self.mac_address}' )
            variable_names = ('snmpMode', 'ipAddress', 'subnetMask', 'defaultGateway', 'ipMethod')
            variables = { name : Variable( station, name) for name in variable_names }
            values = { name : variable.value for name, variable in variables.items() }
                                        
            if intended_ip_method == 0: # fixed IP address -> use the current settings as default
                variables['ipMethod'].value = 0
                variables['ipAddress'].value = values['ipAddress']
                variables['subnetMask'].value = values['subnetMask']
                variables['defaultGateway'].value = values['defaultGateway']
                self.logInfo( 'wait until fixed IP was set')                
            elif intended_ip_method == 1: # DHCP client                                                
                self.logInfo( 'wait until DHCP-Client is active')                
                variables['ipMethod'].value = 1  
                start = time.time()
                while( (time.time()-start ) < 10 ):
                    self.update_idletasks()
                    self.pvi_connection.doEvents()

            self.refreshWidgets(station)
            self.ok_button.config( state='normal')               
        except PviError as e:
            self.logInfo( f'PviError: {e.number}')
        finally: 
            for v in variables.values():
                v.kill()
            station.kill()

        
    def onOkClicked(self):
        self.result = False
        if self.network_settings_changed:
            if self.ip_method_var.get() == self.ip_method_alternatives[0]: # fixed IP ?
                self.onChangeNetworkSettings()
            self.result = True
        self.device.kill()
        self.line.kill()
        self.destroy()
  
    
    def onCancelClicked(self):
        self.result = False   
        self.device.kill()
        self.line.kill()             
        self.destroy()

