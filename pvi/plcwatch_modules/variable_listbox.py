import tkinter as tk
from tkinter import ttk
from typing import Union, Callable, Any
from pvi import Connection, Device, Cpu, Task, Variable

class VariableListBox(ttk.Treeview):
    def __init__(self, parent : tk.Widget,
                 yscrollcommand: Union[str,Callable[[float, float],object]],
                 pvi_connection : Connection
                 ):
        super().__init__( parent, 
                         columns=('cpu', 'name', 'type', 'value'), 
                         show='headings',
                         yscrollcommand=yscrollcommand
                         )        
        self.pvi_connection = pvi_connection
               
        # Configure column headings
        self.heading('cpu', text='Cpu')        
        self.heading('name', text='Name')
        self.heading('type', text='Type')
        self.heading('value', text='Value')
        
        # Configure column widths
        self.column('cpu', width=50, anchor='w')
        self.column('name', width=150, anchor='w')
        self.column('type', width=50, anchor='center')
        self.column('value', width=50, anchor='w')
                
        self.bind('<ButtonRelease-1>', self.onItemDropped)
        self.bind('<B1-Motion>', self.onItemDragged)
        self.bind('<Enter>', self.onEnterWindow)
        self.bind('<Leave>', self.onLeaveWindow)            
        
        self.announced_item : Union[str, None] = None
        self.dragged_item = None
        self.watch_list = dict()
            
    def onEnterWindow( self, event ):
        if self.announced_item:
            item = self.announced_item
            if item not in self.watch_list:
                pvi_object = self.pvi_connection.findObjectByName(item)
                if isinstance( pvi_object, Variable ):
                    assert(pvi_object._parent)
                    variable = Variable( pvi_object._parent, pvi_object.objectName)
                    task : Task = variable._parent # type: ignore
                    taskname = task.objectName.replace('__', '::')
                    cpu : Cpu = task._parent # type: ignore
                    def callback( variable : Variable, value : Any):
                        self.changeValue( variable.name, value )
                    callback( variable, variable.value )
                    variable.valueChanged = callback
                    self.watch_list.update( { item : [variable, callback]})
                    self.insert('', 'end', iid=item, values = [f'{cpu.objectName.replace('_','.')}',
                                                               f'{taskname}:{variable.objectName}', 
                                                               variable.dataType, 
                                                               ''] )
                self.announced_item = None
        
    def onLeaveWindow( self, event):
        self.announced_item = None  
        if self.dragged_item:
            self.delete(self.dragged_item) 
            self.watch_list.pop(self.dragged_item)
            self.dragged_item = None
           
    def changeValue(self, iid : str, value ):
        try:
            values = self.item(iid)['values']
            values[3] = value # type: ignore
            self.item( iid, values = values )           
        except:
            pass
            
    def onItemDropped(self, event ):
        self.config(cursor='')
        if self.dragged_item:
            target_item = self.identify_row(event.y)
            if target_item != '':
                index = self.index(target_item)
                self.move(self.dragged_item, '', index)
                pass
    
    def onItemDragged(self, event):
        item = self.selection()[0] if self.selection() else None
        if item:
            self.config(cursor='exchange')             
            self.dragged_item = item
            
    def announceItem(self, item : str ):
        self.announced_item = item