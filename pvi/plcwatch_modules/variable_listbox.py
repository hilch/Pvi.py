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
from tkinter import ttk, messagebox, font
from typing import cast, Union, Callable, Any
from pvi import Connection, PviObject, Cpu, Task, Variable

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
        self.column('value', width=100, anchor='w')
                
        self.bind('<ButtonRelease-1>', self.onItemDropped)
        self.bind('<B1-Motion>', self.onItemDragged)
        self.bind('<Enter>', self.onEnterWindow)
        self.bind('<Leave>', self.onLeaveWindow) 
        self.bind('<Double-1>', self.onDoubleClick)                      
        
        self.announced_pvi_object : Union[PviObject, None] = None
        self.dragged_item = None
        self.watch_list = dict()
        self.watch_value_entry = tk.Entry(self)

            
    def onEnterWindow( self, event ):
        if isinstance( self.announced_pvi_object, Variable):
            variable = cast( Variable, self.announced_pvi_object)
            if variable.name not in self.watch_list:
                # add variable to watch list
                task : Task = cast(Task, variable._parent)
                taskname = task.objectName.replace('__', '::')
                cpu : Cpu = task._parent # type: ignore
                self.onValueChanged( variable, variable.value )
                variable.valueChanged = self.onValueChanged
                variable.errorChanged = self.onErrorChanged                                
                self.watch_list.update( { variable.name : [variable]})
                self.insert('', 'end', iid=variable.name, values = [f'{cpu.objectName.replace('_','.')}',
                                                            f'{taskname}:{variable.objectName}', 
                                                            variable.dataType, variable.value] )
            self.announced_pvi_object = None
    
        
    def onLeaveWindow( self, event):
        self.announced_pvi_object = None  
        if self.dragged_item:
            self.delete(self.dragged_item) 
            self.watch_list.pop(self.dragged_item)
            self.dragged_item = None
    
    
    def onDoubleClick(self, event : tk.Event):
        item = self.identify('item', event.x, event.y)
        column = self.identify_column(event.x)
        if item:
            o = self.watch_list[item][0]
            if isinstance(o, Variable) and column == '#4':
                variable = cast( Variable, o)
                current_value = self.item(item)['values'][3]
                # set current value as default
                self.watch_value_entry.delete(0,'end')
                self.watch_value_entry.insert(0, current_value )
                self.watch_value_entry.select_range(0,'end')
                bbox = self.bbox(item, column)
                if bbox:
                    self.watch_value_entry.place(x=bbox[0], y=bbox[1], width=bbox[2], height=bbox[3])
                self.watch_value_entry.focus()
                def hide_edit(event=None):
                    self.watch_value_entry.place_forget()
                    self.watch_value_entry.unbind_all('<Return>')
                    self.watch_value_entry.unbind_all('<FocusOut>')                
                def save_edit(event=None):
                    str_value = self.watch_value_entry.get()
                    try:
                        variable.parseIEC( str_value)
                    except (ValueError, TypeError) as e:
                        messagebox.showerror( 'Error', str(e))
                    hide_edit()
                self.watch_value_entry.bind('<Return>', save_edit)
                self.watch_value_entry.bind('<FocusOut>', hide_edit)    
    
    
    def onErrorChanged( self, object : PviObject,  error : int ):
        if error == 11022:
            self.displayItemValue( object.name, 'OFFLINE')
            return
    
    def onValueChanged( self, variable : Variable, value : Any):
        self.displayItemValue( variable.name, variable.toIEC() )
    
           
    def displayItemValue(self, iid : str, value ):
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
            
    def announcePviObject(self, object : PviObject ):
        self.announced_pvi_object = object