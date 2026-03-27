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
from collections import OrderedDict 
from typing import cast, Any, Union, Callable
from ipaddress import IPv4Address
import re
import json
import time
from pvi import Connection, PviObject, Device, Cpu, Task, Variable, PviError
from pvi.plcwatch_modules.resources import image_files
from pvi.plcwatch_modules.treeview_tooltip import TreeViewTooltip
from pvi.plcwatch_modules.edit_cpu_dialog import EditCpuDialog 
from pvi.plcwatch_modules.time_dialog import TimeDialog
from pvi.utils.IEC import toIEC

class ObjectTreeView(ttk.Treeview):
    def __init__(self, parent : tk.Widget, 
                 yscrollcommand: Union[str,Callable[[float, float],object]],
                 pvi_connection : Connection, 
                 callback_ip_connected : Callable[[str],None],
                 callback_mouse_leave: Callable[[PviObject],None] 
                ):
        super().__init__( parent, 
                         columns=('name', 'type','value'), 
                         show=('tree','headings'),                         
                         selectmode='browse', 
                         yscrollcommand=yscrollcommand
                         )
       
        self.last_update = time.time()
        self.tooltip_handler = TreeViewTooltip(self)
        self.pvi_connection = pvi_connection        
        self.callback_ip_connected = callback_ip_connected 
        self.callback_mouse_leave = callback_mouse_leave       
        self.image_storage = { str(k) : tk.PhotoImage( file = v ) for k,v in image_files.items() }        
        
        self.heading('#0', text='Name')
        self.heading('#1', text='Type')        
        self.heading('#2', text='Value')
        
        self.column('#0', width=150, anchor='w')
        self.column('#1', width=70, anchor='center')
        self.column('#2', width=150, anchor='w')     
        self.column('#3', width=0)            
        
        self.bind('<<TreeviewSelect>>', self.onItemSelected)
        self.bind("<<TreeviewOpen>>", self.onItemOpened )
        self.bind("<<TreeviewClose>>", self.onItemClosed)
        self.bind("<B1-Motion>", self.onItemDragged)     
        self.bind('<ButtonRelease-1>', self.onButtonRelease1)  
        self.bind('<Leave>', self.onMouseLeave)        
        self.bind("<Button-3>", self.onButton3) 
        self.bind('<Double-1>', self.onDoubleClick)            
                   
        self.watch_list = dict()
        self.watch_value_entry = tk.Entry(self)
        
        self.selected_item = None
        self.dragged_item = None
              
        # Create context menus
        self.context_menu_cpu = tk.Menu(self, tearoff=False)
        self.context_menu_cpu.add_command(label="Edit (SNMP) ", command= lambda c = 'edit': self.onCpuContextMenu(c))
        self.context_menu_cpu.add_command(label="Date/ Time", command= lambda c = 'date_time': self.onCpuContextMenu(c))
        self.context_menu_cpu.add_separator()                      
        self.context_menu_cpu.add_command(label="Warmstart", command= lambda c = 'warmstart': self.onCpuContextMenu(c))
        self.context_menu_cpu.add_command(label="Coldstart", command= lambda c = 'coldstart': self.onCpuContextMenu(c))
        self.context_menu_cpu.add_command(label="Service", command= lambda c = 'stop': self.onCpuContextMenu(c))        
        self.context_menu_cpu.add_command(label="Diag", command= lambda c = 'diag': self.onCpuContextMenu(c))  
        self.context_menu_cpu.add_separator()
        self.context_menu_cpu.add_command(label="Remove", command= lambda c = 'remove': self.onCpuContextMenu(c))                     

        self.context_menu_task = tk.Menu(self, tearoff=False)
        self.context_menu_task.add_command(label="Start", command= lambda c = 'start': self.onTaskContextMenu(c))
        self.context_menu_task.add_command(label="Stop", command= lambda c = 'stop': self.onTaskContextMenu(c))
        self.context_menu_task.add_command(label="Resume", command= lambda c = 'resume': self.onTaskContextMenu(c))
        self.context_menu_task.add_command(label="1 Cycle", command= lambda c = 'cycle1': self.onTaskContextMenu(c))     
                
             
    def update(self):
        t = time.time()
        if (t - self.last_update) > 5:
            self.last_update = t
            for iid, data in self.watch_list.items():
                iid : str
                data : list
                object = data[0]
                if isinstance( object, Task):
                    object.readRequestStatus( self.statusResponse )
                
        
    def expandStruct( self, task : Task, struct : Variable):
        '''
        expand a structure to its elements.
        
            Args:
                task : task containing this structure
                struct : structure variable itself
        ''' 
        
        struct_elements = dict.fromkeys( '.' + re.split(r'[\[.]', e[1:])[0] for e in struct.value )
            
        for counter, element_name in enumerate(struct_elements):
            # if counter % 10 == 0:
            #     self.update_idletasks()  
            element = Variable(task, struct.objectName + element_name)
            
            icon = self.image_storage.get(element.dataType, self.image_storage['variable'])

            tags = [f'"type":"variable","task-linkid":{task._linkID},"varname":"{struct.objectName}{element_name}"']
            iid = element.name
            if element.isArray:
                # insert array variable itself
                self.insert( struct.name, index = 'end', 
                                iid = iid, text = element_name,
                            image = self.image_storage['array'], tags=tags,
                            values=[element.dataType] ) 
                self.tooltip_handler.set_tooltip(iid, iid)   
                # insert array elements
                self.expandArray( task, element )        
            elif element.isStructure:
                # insert the substructure itself
                self.insert( struct.name, index = 'end', 
                                         iid = iid, text = element_name,
                            image = self.image_storage['struct'], tags=tags,
                            values=[element.dataType] ) 
                self.tooltip_handler.set_tooltip(iid, iid)   
                #self.expandStruct(task, element)           
            else: 
                self.insert( struct.name, index = 'end', iid = iid, text = element_name,
                                    image = icon, tags=tags, 
                                    values=[element.dataType, element.value] )  
                self.tooltip_handler.set_tooltip(iid, iid) 
            element.kill() 
        
        
    def expandArray( self, task : Task, array : Variable):
        '''
        expands an array variable.
        
            Args:
            
            task : task containing
            values : elements' values
        '''
        
        datatype_name = array.dataType.split('[')[0]
        icon = self.image_storage.get(datatype_name, self.image_storage['variable'])
        
        indices = array._type_description.get_array_indices()
        assert(indices)
        for j, v in enumerate(array.value):
            # if j % 10 == 0:
            #     self.update_idletasks()             
            if isinstance( v, list ): # two-dimensional array ?
                for k, vk in enumerate(v):
                    i1 = indices[0][0] + j
                    i2 = indices[1][0] + k
                    tags = [f'"type":"variable","task-linkid":{task._linkID},"varname":"{array.objectName}[{i1},{i2}]"']
                    if isinstance( vk, OrderedDict ):
                        #insert struct itself
                        iid = f'{array.name}[{i1},{i2}]'
                        self.insert( array.name, index = 'end', 
                            iid = iid, text = f'[{i1},{i2}]',
                            image = self.image_storage['struct'], tags = tags )
                        self.tooltip_handler.set_tooltip(iid, iid)
                    else:
                        iid = f'{array.name}[{i1},{i2}]'
                        self.insert( array.name, index = 'end', 
                                iid = iid, text = f'[{i1},{i2}]',
                                image = icon, values = [datatype_name, vk] )
                        self.tooltip_handler.set_tooltip(array.name, array.name)
            else: # vector
                # self.update_idletasks()             
                i1 = indices[0][0] + j
                tags = [f'"type":"variable","task-linkid":{task._linkID},"varname":"{array.objectName}[{i1}]"']
                iid = f'{array.name}[{i1}]'
                if isinstance( v, OrderedDict):
                    #insert struct itself
                    self.insert( array.name, index = 'end', 
                        iid = iid, text = f'[{i1}]',
                        image = self.image_storage['struct'], tags = tags )
                    self.tooltip_handler.set_tooltip(iid, iid)
                else:           
                    self.insert( array.name, index = 'end', 
                            iid = f'{array.name}[{i1}]', text = f'[{i1}]',
                            image = icon, tags = tags,
                            values = [datatype_name, v] )
                    self.tooltip_handler.set_tooltip(iid, iid)
        
        
    def onTaskClicked( self, item : str, task : Task ):
        if not self.get_children(item):
            variableNames = task.variables
            for name in variableNames:
                variable = Variable(task, name)
                icon = self.image_storage.get(variable.dataType, self.image_storage['variable'])
                 
                value = variable.value
                tags = [f'"type":"variable","task-linkid":{task._linkID},"varname":"{name}"']
                if variable.isArray: # is variable an array ?
                    # insert array itself
                    self.insert( item, index = 'end', iid = variable.name, text = name, tags=tags,
                                image = self.image_storage['array'], values=[variable.dataType] )
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                    self.expandArray(task,variable)                
                elif variable.isStructure: # is variable a struct ?
                    # insert struct itself
                    self.insert( item, index = 'end', iid = variable.name, text = name, tags=tags,
                                image = self.image_storage['struct'], values=[variable.dataType] )    
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                    # insert children
                    self.expandStruct(task, variable)
                else: # variable with basic datatype        
                    self.insert( item, index = 'end', iid = variable.name, text = name, tags=tags,
                                image = icon, values = [variable.dataType, value] )    
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                variable.kill()       
        
    def onItemSelected( self, event ):
        # Change cursor to hourglass/watch during execution
        self.config(cursor="watch")
        self.update_idletasks()  # Force cursor update
        
        try:
            item = self.selection()[0] if self.selection() else None
            if item:
                tags = self.item( item, 'tags' )
                meta = json.loads( '{' + tags[0] + '}')
             
                if meta['type'] == 'task':
                    task = cast( Task, self.pvi_connection.findObjectByLinkID(meta['task-linkid']))
                    self.onTaskClicked( item, task ) 
                elif meta['type'] == 'variable':
                    task = cast( Task, self.pvi_connection.findObjectByLinkID(meta['task-linkid']) )
                    variable = Variable( task, meta['varname'])
                                        
                    if not variable.isArray and not variable.isStructure:
                        self.selected_item = item 
                    else:                                              
                        if variable.isArray and not self.get_children(item):
                            self.expandArray( task, variable ) 
                        if variable.isStructure and not self.get_children(item):
                            self.expandStruct( task, variable )             
                    variable.kill()              
        except Exception as e:
            pass
        finally:
            # Restore cursor to default
            self.config(cursor="")
            self.update_idletasks()


    def onItemDragged( self, event ):
        if self.selected_item:
            self.config(cursor='exchange')   
            self.dragged_item = self.selected_item
            self.selected_item = None

            
    def onButtonRelease1( self, event ):
        # Restore cursor to normal
        self.config(cursor="")
        self.selected_item = None
        self.dragged_item = None

         
    def onMouseLeave( self, event ):
        if self.dragged_item:
            self.config(cursor='hand2')
            tags = self.item( self.dragged_item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}') 
            if meta['type'] == 'variable':
                task = cast( Task, self.pvi_connection.findObjectByLinkID( meta['task-linkid']))
                variable = Variable( task, meta['varname'], RF=200)
                self.callback_mouse_leave(variable)

        
    def onItemOpened(self, event):
        """Called when parent item is expanded"""
        self.config(cursor="watch")
        self.update_idletasks()          
        #tree = event.widget
        item = self.selection()[0] if self.selection() else None
    
        if item:
            tags = self.item( item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}')   
            if meta['type'] == 'cpu':
                pass
            elif meta['type'] == 'task':
                task = self.pvi_connection.findObjectByLinkID(meta['task-linkid'])                 
                children = self.get_children(item)                
                for counter, child in enumerate(children):
                    tags = self.item( child, 'tags' )
                    try:
                        meta = json.loads( '{' + tags[0] + '}')   
                    except Exception as e:
                        pass
                    variable = Variable( task, meta['varname'], RF=200 )
                    self.onValueChanged( variable, variable.value )
                    variable.valueChanged = self.onValueChanged
                    variable.errorChanged = self.onErrorChanged
                    self.watch_list.update( { child : [variable]})
            elif meta['type'] == 'variable':
                pass
                            
            self.config(cursor='') # restore cursor
            self.update_idletasks()  


    def onItemClosed(self, event):
        """Called when parent item is collapsed"""
        #tree = event.widget
        item = self.selection()[0] if self.selection() else None
        
        if item:
            tags = self.item( item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}')  
            self.removeChildrenFromWatchList(item)      
                    
                    
    def removeChildrenFromWatchList(self, item : str):
        """Remove descendant variables from watchlist"""
        children = self.get_children(item)
        for child in children:
            self.item( child, open=False) # close item
            self.removeChildrenFromWatchList(child) # remove all children
            if child in self.watch_list:
                object : PviObject = self.watch_list[child][0]
                object.kill()
                self.watch_list.pop(child)
                self.delete(child)
        
       
    def onErrorChanged( self, object : PviObject,  error : int ):
        if error == 11022:
            self.displayItemValue( object.name, 'OFFLINE')
            return
        if isinstance( object, Cpu ):
            cpu = cast( Cpu, object )
            if error == 11020:
                cpu.kill()
            elif error == 0:
                if self.exists( cpu.name ):
                    self.item( cpu.name, values = [ cpu.cpuInfo.get('CT', 'unknown'), cpu.status.get('RunState','unknown') ])
                else:
                    self.watch_list.update( {cpu.name : [cpu] })
                    tags = [f'"type":"cpu", "cpu":"{cpu.objectName}"']
                    iid = cpu.name
                    self.insert('', index = 'end', iid = iid, text=cpu.objectName.replace('_','.'), 
                                image=self.image_storage['cpu'], tags = tags,
                                values = [ cpu.cpuInfo.get('CT', 'unknown'), cpu.status.get('RunState','unknown') ])
                    self.tooltip_handler.set_tooltip(iid, iid)
                    self.insertTasks(cpu)                   
            else:
                values = self.item(cpu.name)['values']
                values[1] = f'Pvi-Error: {error}' # type: ignore
                self.item( cpu.name, values = values)  


    def onValueChanged( self, variable : Variable, value : Any):
        if isinstance( value, list ): # array ?
            self.displayItemValuesIfArray( variable.name, value )
        elif isinstance( value, OrderedDict): # structure ?
            self.displayItemValuesIfStructure( variable.name, value )
        else:
            self.displayItemValue( variable.name, variable.toIEC() )
    
    
    def statusResponse( self, object : PviObject, status : dict ):
        if isinstance( object, Task ):
            self.displayItemValue( object.name, status.get('ST'))         
    
    
    def displayItemValue(self, iid : str, value : Any):
        values = self.item(iid)['values']
        values[1] = value # type: ignore
        self.item( iid, values = values )
     
          
    def displayItemValuesIfStructure(self, iid : str, struct_values : OrderedDict ):
        for element, element_value in struct_values.items():

            if isinstance( element_value, list ):
                if self.exists( iid + element ):               
                    self.displayItemValuesIfArray( iid + element, element_value )
            else:
                if self.exists( iid + element ):
                    self.displayItemValue( iid + element, toIEC(element_value) )                    
    
    
    def displayItemValuesIfArray(self, iid: str, list_values : list):
        children = self.get_children(iid)
        for index, value in enumerate(list_values):
            if isinstance( value, list): # two-dimensional array ?
                length = len(value)
                for index2, v in enumerate(value):
                    self.displayItemValue( children[index*length+index2], v)    
            else:          
                self.displayItemValue( children[index], value)
    
        
        
    def insertCpu(self, device : Device, ip : IPv4Address ):
        name = ip.compressed.replace('.','_')
        cpu = Cpu( device, name, CD=f"/IP={ip.compressed} /SDT=5 /PVROI=1 /COMT=3000" )
        setattr( cpu, 'ip', ip.compressed )
        cpu.errorChanged = self.onErrorChanged
        
        
    def insertTasks(self, cpu : Cpu ):
        allObjects = cpu.externalObjects
        # read task names
        taskNames = [ _['name'] for _ in allObjects if _['type'] == 'Task'] 
        for name in taskNames:  # read the tasks' status
            task = Task( cpu, name.replace('::','__'), CD=f'"{name}"' )

            tags = [f'"type":"task", "cpu":"{cpu.objectName}","task-linkid":{task._linkID}']
            iid = f'{task.name}'
            self.insert( cpu.name, index = 'end', iid = iid, text = name,
                        image = self.image_storage['task'], tags= tags,
                        values = ['Task', task.status['ST']] )    
            self.tooltip_handler.set_tooltip(iid, iid)
            # define callbacks for status and error event
            task.errorChanged = self.onErrorChanged
            self.watch_list.update( { task.name : [task]})                                         
        ip = getattr( cpu, 'ip')
        self.callback_ip_connected(ip)        
        
        
    def onButton3(self, event : tk.Event):
        # Select item at cursor position
        item = self.identify('item', event.x, event.y)
        if item:
            self.selection_set(item)
            self.selected_item = item
            tags = self.item( item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}')   
            if meta['type'] == 'cpu':
                self.context_menu_cpu.post(event.x_root, event.y_root) 
            elif meta['type'] == 'task':
                     self.context_menu_task.post(event.x_root, event.y_root) 
     
     
    def onDoubleClick(self, event : tk.Event):
        item = self.identify('item', event.x, event.y)
        column = self.identify_column(event.x)
        if item:
            tags = self.item( item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}')
            if meta['type'] == 'variable' and column == '#2': # clicked on variable's value field
                task = cast( Task, self.pvi_connection.findObjectByLinkID(meta['task-linkid']))
                variable = Variable( task, meta['varname'])
                current_value = self.item(item)['values'][1]
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
                    variable.kill()               
                def save_edit(event=None):
                    str_value = self.watch_value_entry.get()
                    try:
                        variable.parseIEC( str_value)
                    except (ValueError, TypeError) as e:
                        messagebox.showerror( 'Error', str(e))
                    hide_edit()
                self.watch_value_entry.bind('<Return>', save_edit)
                self.watch_value_entry.bind('<FocusOut>', hide_edit)
              
        
        
    def onCpuContextMenu( self, type : str):
        item = self.selected_item
        if item:           
            try:
                cpu : Cpu = cast( Cpu, self.pvi_connection.findObjectByName(item))
            except KeyError:
                return
            try:
                is_online = True
                _ = cpu.status
            except PviError as e:
                if e.number == 11022:
                    is_online = False

            if is_online: 
                if type == 'edit':
                    dialog = EditCpuDialog(self, self.pvi_connection, cpu )
                    self.wait_window(dialog)
                elif type == 'date_time':
                    dialog = TimeDialog(self, self.pvi_connection, cpu )
                elif type == 'warmstart':
                    cpu.warmStart()
                elif type == 'coldstart':
                    cpu.coldStart()
                elif type == 'stop':
                    cpu.stopTarget()
                elif type == 'diag':
                    cpu.diagnostics()
            if type == 'remove':
                self.removeChildrenFromWatchList(cpu.name)
                self.delete(cpu.name) # remove from tree            
                self.watch_list.pop(cpu.name) # remove from watch list           
                cpu.kill() # remove PVI-Object

        
    def onTaskContextMenu( self, type : str):
        item = self.selected_item
        if item:           
            try:
                task : Task = cast( Task, self.pvi_connection.findObjectByName(item))
            except KeyError:
                return
            try:
                is_online = True
                _ = task.status
            except PviError as e:
                if e.number == 11022:
                    is_online = False

            if is_online: 
                if type == 'start':
                    task.status = 'Start'
                elif type == 'stop':
                    task.status = 'Stop'
                elif type == 'resume':
                    task.status = 'Resume'
                elif type == 'cycle1':
                    task.status = 'Cycle(1)'