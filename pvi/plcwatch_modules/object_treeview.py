import tkinter as tk
from tkinter import ttk
from collections import OrderedDict 
from typing import List, Any, Union, Callable
from ipaddress import IPv4Address
import re
import json
from pvi import Connection, Device, Cpu, Task, Variable
from pvi.plcwatch_modules.resources import image_files
from pvi.plcwatch_modules.treeview_tooltip import TreeViewTooltip


class ObjectTreeView(ttk.Treeview):
    def __init__(self, parent : tk.Widget, 
                 yscrollcommand: Union[str,Callable[[float, float],object]],
                 pvi_connection : Connection, 
                 callback_ip_connected : Callable[[str],None],
                 callback_mouse_leave: Callable[[str],None] 
                ):
        super().__init__( parent, 
                         columns=('name', 'type', 'value'), 
                         selectmode='browse', 
                         yscrollcommand=yscrollcommand
                         )
        self.tooltip_handler = TreeViewTooltip(self)
        self.pvi_connection = pvi_connection        
        self.callback_ip_connected = callback_ip_connected 
        self.callback_mouse_leave = callback_mouse_leave       
        self.image_storage = { str(k) : tk.PhotoImage( file = v ) for k,v in image_files.items() }        
        
        self.heading('#0', text='Name')
        self.heading('#1', text='Type')        
        self.heading('#2', text='Value')
        self.bind('<<TreeviewSelect>>', self.onItemSelected)
        self.bind("<<TreeviewOpen>>", self.onItemOpened )
        self.bind("<<TreeviewClose>>", self.onItemClosed)
        self.bind("<B1-Motion>", self.onItemDragged)     
        self.bind('<ButtonRelease-1>', self.onButtonRelease1)  
        self.bind('<Leave>', self.onMouseLeave)        
          
                   
        self.cpu_list : List[Cpu] = []
        self.watch_list = dict()
        
        self.selected_item = None
        self.dragged_item = None
              
        
    def expandStruct( self, task : Task, struct : Variable):
        '''
        expand a structure to its elements.
        
            Args:
                task : task containing this structure
                struct : structure variable itself
        ''' 
        struct_elements = dict.fromkeys( '.' + re.split(r'[\[.]', e[1:])[0] for e in struct.value )
            
        for element_name in struct_elements:
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
        
        icon = self.image_storage.get(array.dataType.split('[')[0], self.image_storage['variable'])
        
        indices = array._type_description.get_array_indices()
        assert(indices)
        for j, v in enumerate(array.value):
            if isinstance( v, list ): # two-dimensional array ?
                for k, vk in enumerate(v):
                    i1 = indices[0][0] + j
                    i2 = indices[1][0] + k
                    tags = [f'"type":"varable","task-linkid":{task._linkID},"varname":"{array.objectName}[{i1},{i2}]"']
                    if isinstance( vk, OrderedDict ):
                        #insert struct itself
                        iid = f'{task.name}/{array.name}[{i1},{i2}]'
                        self.insert( array.name, index = 'end', 
                            iid = iid, text = f'[{i1},{i2}]',
                            image = self.image_storage['struct'], tags = tags )
                        self.tooltip_handler.set_tooltip(iid, iid)
                    else:
                        iid = f'{array.name}[{i1},{i2}]'
                        self.insert( array.name, index = 'end', 
                                iid = iid, text = f'[{i1},{i2}]',
                                image = icon, values = vk )
                        self.tooltip_handler.set_tooltip(array.name, array.name)
            else: # vector
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
                            values = v )
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
                self.selected_item = item                
                if meta['type'] == 'task':
                    task = self.pvi_connection.findObjectByLinkID(meta['task-linkid']) 
                    self.onTaskClicked( item, task ) # type: ignore
                elif meta['type'] == 'variable':
                    task = self.pvi_connection.findObjectByLinkID(meta['task-linkid']) 
                    variable = Variable( task, meta['varname'])
                    if variable.isArray and not self.get_children(item):
                        self.expandArray( task, variable ) # type: ignore
                    if variable.isStructure and not self.get_children(item):
                        self.expandStruct( task, variable ) # type: ignore      
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
            self.callback_mouse_leave(self.dragged_item)
        

    def onItemOpened(self, event):
        """Called when parent item is expanded"""
        #tree = event.widget
        item = self.selection()[0] if self.selection() else None
    
        if item:
            tags = self.item( item, 'tags' )
            meta = json.loads( '{' + tags[0] + '}')   
            if meta['type'] == 'cpu':
                return
            task = self.pvi_connection.findObjectByLinkID(meta['task-linkid']) 

            # Get all children
            children = self.get_children(item)
            for child in children:
                tags = self.item( child, 'tags' )
                try:
                    meta = json.loads( '{' + tags[0] + '}')   
                except Exception as e:
                    pass
                variable = Variable( task, meta['varname'], RF=200 )
                if not(variable.isArray) and not(variable.isStructure):
                    def callback( variable : Variable, value : Any):
                        self.changeValue( variable.name, value )
                    callback( variable, variable.value )
                    variable.valueChanged = callback
                    self.watch_list.update( { child : [variable, callback]})
                else:
                    variable.kill() # immediately kill variable in case of complex type


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
            if child in self.watch_list:
                variable : Variable = self.watch_list[child][0]
                variable.kill()
            self.removeChildrenFromWatchList(child)    
        
       
    def cpuErrorChanged( self, cpu : Cpu,  error : int ):
        if error == 11020:
            print("Unable to establish connection")
        elif error != 0:
            pass
        else:
            self.cpu_list.append(cpu)
            tags = [f'"type":"cpu", "cpu":"{cpu.objectName}"']
            iid = cpu.name
            parent = self.insert('', index = 'end', iid = iid, text=cpu.objectName.replace('_','.'), 
                        image=self.image_storage['cpu'], tags = tags,
                        values = [ cpu.cpuInfo.get('CT', 'unknown'), cpu.status.get('RunState','unknown') ])
            self.tooltip_handler.set_tooltip(iid, iid)
            allObjects = cpu.externalObjects
            # read task names
            taskNames = [ _['name'] for _ in allObjects if _['type'] == 'Task'] 
            for name in taskNames:  # read the tasks' status
                task = Task( cpu, name.replace('::','__'), CD=f'"{name}"' )
                task_status = task.status['ST']
                tags = [f'"type":"task", "cpu":"{cpu.objectName}","task-linkid":{task._linkID}']
                iid = f'{task.name}'
                self.insert( parent, index = 'end', iid = iid, text = name,
                            image = self.image_storage['task'], tags= tags,
                            values = ['Task', task_status] )    
                self.tooltip_handler.set_tooltip(iid, iid)
            ip = getattr( cpu, 'ip')
            self.callback_ip_connected(ip)
    
    
    def changeValue(self, iid : str, value ):
        values = self.item(iid)['values']
        values[1] = value # type: ignore
        self.item( iid, values = values )
            
        
    def insertCpu(self, device : Device, ip : IPv4Address ):
        name = ip.compressed.replace('.','_')
        cpu = Cpu( device, name, CD=f"/IP={ip.compressed} /SDT=5 /PVROI=1 /COMT=10000" )
        setattr( cpu, 'ip', ip.compressed )
        cpu.errorChanged = self.cpuErrorChanged
        
   
        
