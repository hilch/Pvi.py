import tkinter as tk
from tkinter import ttk
from typing import cast, Callable
from pvi import Connection, Line, PviObject, Device, Station, Cpu, Task, Variable
from .resources import icon_storage

class EditCpuDialog():
    def __init__(self, parent, pvi_connection : Connection, cpu : Cpu ):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Edit CPU")
        self.dialog.geometry("400x500")
        self.dialog.resizable(False, False)       
        self.dialog.iconbitmap(icon_storage['cpu'])
        self.dialog.grid_rowconfigure(0, weight=1)
        self.dialog.grid_columnconfigure(0, weight=1)        
        
        self.line = Line( pvi_connection.root, 'LNSNMP', CD='LNSNMP')
        self.device = Device( self.line, 'Device', CD='/IF=snmp /RT=1000' )
        self.device.errorChanged =cast( Callable[[PviObject,int],None], self.deviceErrorChanged)
        
        self.cpu = cpu
        cpu_info_extended = cpu.cpuInfoExtended        
        self.ip_address = self.cpu.objectName.replace('_','.') 
        
        # Variables
        self.ip_method_var = tk.BooleanVar()
        self.ina_activated_var = tk.BooleanVar()        
        
        # Create main frame
        main_frame = ttk.Frame(self.dialog, padding="10")
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
        
        # ===== Network Settings =====
        row+=1
        ttk.Label(main_frame, text='Network Settings', font=('Arial', 10, "bold")).grid(row=row, column=0, pady=(15, 10), sticky="w")

        row+=1
        self.ip_method = ttk.Checkbutton(main_frame, text="DHCP-Client", variable=self.ip_method_var)
        self.ip_method.grid(row=row, column=0, columnspan=2, sticky="w")         
        
        row+=1
        ttk.Label(main_frame, text='IP:').grid(row=row, column=0, sticky="w")
        self.ip_entry = ttk.Entry(main_frame)
        self.ip_entry.insert(0, self.ip_address)
        self.ip_entry.grid(row=row, column=1, sticky="ew", padx=5 )
              
        row+=1       
        ttk.Label(main_frame, text='SUBNET:').grid(row=row, column=0, sticky="w")
        self.subnet_entry = ttk.Entry(main_frame)
        self.subnet_entry.insert(0, '?')
        self.subnet_entry.grid(row=row, column=1, sticky="ew", padx= 5)
        
        row+=1
        ttk.Label(main_frame, text="GATEWAY:").grid(row=row, column=0, sticky="w")
        self.gateway_entry = ttk.Entry(main_frame)
        self.gateway_entry.insert(0, "?")
        self.gateway_entry.grid(row=row, column=1, sticky="ew", padx=5)
        
        
        # ===== INA =====
        
        row+=1
        self.snmp_check = ttk.Checkbutton(main_frame, text="INA activated", variable=self.ina_activated_var)
        self.snmp_check.grid(row=row, column=0, columnspan=2, sticky="w")
                
        row+=1
        ttk.Label(main_frame, text="INA Node Number").grid(row=row, column=0, sticky="w")
        self.ina_node_number_label = ttk.Label(main_frame, text='?', relief="sunken")
        self.ina_node_number_label.grid(row=row, column=1, sticky="ew", padx=5 )         

        # ==== Options ====
        row+=1
        ttk.Label(main_frame, text="Options", font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=2, pady=(15, 10), sticky="w")
            
        row+=1        
        ttk.Label(main_frame, text="SNMP-Mode").grid(row=row, column=0, sticky="w")
        self.snmpmode_label = ttk.Label(main_frame, text="deactivated", relief="sunken")
        self.snmpmode_label.grid(row=row, column=1, sticky="ew", padx=5 )       
        

        
        # ===== Buttons =====
        row+=1
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=(15, 0), sticky="ew")
        
        ok_button = ttk.Button(button_frame, text="OK", command=self.ok_clicked)
        ok_button.pack(side="left", padx=5)
        
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.cancel_clicked)
        cancel_button.pack(side="left", padx=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        
        # Make dialog non-modal (user can interact with parent window)
        self.dialog.grab_release()
    
    
    def deviceErrorChanged( self, device : Device, error : int ):
        
        if error == 0:
            macs = [ x['name'] for x in device.externalObjects if x['type'] == 'Station']
            for mac in macs:
                station = Station( device, 'station', CD=f'/CN={mac}' )
                variables = { o['name'] : Variable( station, o['name']) for o in station.externalObjects }
                              
                if variables['ipAddress'].value == bytes(self.ip_address,'ascii'):
                    self.mac_label.config( text = mac )
                    
                    self.serial_number.config( text = variables['serialNumber'].value )
                    
                    self.ip_method_var.set( variables['ipMethod'].value )                
                    
                    self.subnet_entry.delete(0,'end')
                    self.subnet_entry.insert(0, variables['subnetMask'].value )
                    
                    self.gateway_entry.delete(0,'end')
                    self.gateway_entry.insert(0, variables['defaultGateway'].value )
                    
                    try:
                        self.node_number_label.config( text = variables['nodeNumber'].value )
                    except:
                        pass
                    
                    self.snmpmode_label.config( text = { 0 : 'deactivated', 1 : 'read-only', 2 : 'activated'}.
                                               get( variables['snmpMode'].value , '?'))
                    
                    self.ina_activated_var.set( variables['inaActivated'].value)
                    
                    try:                  
                        self.ina_node_number_label.config( text = variables['inaNodeNumber'].value )
                    except:
                        pass
                    
                for variable in variables.values():
                    variable.kill()
                station.kill()
        else:
            pass

      
    def ok_clicked(self):
        self.dialog.destroy()
    
    def cancel_clicked(self):
        print("Cancel clicked")
        self.dialog.destroy()

