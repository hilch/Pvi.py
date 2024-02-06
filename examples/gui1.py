# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this example shows the usage of Pvi.py in tkinter
#

import tkinter as tk
import tkinter.ttk as ttk
from pvi import *


class ApplicationWindow(tk.Tk):
    """
    the application's main window
    """
    def __init__(self ):
        super().__init__()

        self.geometry('320x200')
        self.title('coffee machine') 
        self.pviLicense = 'unchecked'

        # setup widgets
        #self.columnconfigure( index = 0, weight= 1)
        self.rowconfigure(4, weight=1)

        self._lblTemperature = tk.Label(self, text="Temperature:")
        self._lblTemperature.grid( row= 0, column= 0 )              
        
        self._outputTemperature = tk.Label(self, text="00.0")
        self._outputTemperature.grid( row= 0, column= 1 )                       

        self._checkTemperatureOk = tk.IntVar(self, 0 )
        self._checkbtnTemperatureOk = ttk.Checkbutton( self, text= 'Ok', takefocus = False, variable = self._checkTemperatureOk )
        self._checkbtnTemperatureOk.grid( row=0, column=2)

        self._btnPowerOn = tk.Button( self, text ="Power On", command = self.actionPowerOn )   
        self._btnPowerOn.grid( row= 3, column= 0 )             

        self._btnPowerOff = tk.Button( self, text ="Power Off", command = self.actionPowerOff )   
        self._btnPowerOff.grid( row= 3, column= 1 )             

        
        # status bar
        self._lblStatusbar = tk.Label(self, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self._lblStatusbar.grid( row= 4, column= 0,sticky='sew' )        

        self.connection = Connection()
        # all PVI objects must be registered hierarchically
        # line ANSL is the 'modern' way to access PLC variables
        # (compared to the older INA2000 line)
        #
        self.line = Line( self.connection.root, 'LNANSL', CD='LNANSL')
        self.device = Device( self.line, 'TCP', CD='/IF=TcpIp' )
        self.cpu = Cpu( self.device, 'myArsim', CD='/IP=127.0.0.1' )
        self.task1 = Task( self.cpu, 'mainlogic')

        self.gHeating = Variable( self.task1, 'gHeating', RF=200 )
        self.gHeating.valueChanged = self.callbackHeating
       
        # we then register a variable to switch on the machine
        self.switchOnOff = Variable( self.task1, 'gMainLogic.cmd.switchOnOff' )        

        self.after( 10, self.update) 
        self.after( 1000, self.checkPviLicense )                      

    def actionPowerOn(self):
        self.switchOnOff.value = True

    def actionPowerOff(self):
        self.switchOnOff.value = False
           
    def callbackHeating(self, value):
        self._outputTemperature.config( text = round( float(value.get('.status.actTemp')), 1) )
        self._checkTemperatureOk.set( int(value.get('.status.setTempOK')) )
        
    def update(self):
        try:
            self.connection.doEvents() # execute PVI event loop
        except:
            pass
        self.after( 100, self.update)  

        
    def checkPviLicense(self):
        li = self.connection.license[0]
        self._lblStatusbar.config( text = 'PVI license: ' + li )        
        self.after( 1000 if li == 'undefined' else 30000 , self.checkPviLicense )                


app = ApplicationWindow()
app.mainloop()