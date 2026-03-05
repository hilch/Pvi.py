import tkinter as tk
from tkinter import ttk
from collections import OrderedDict 
from typing import List, Callable, Any
from ipaddress import IPv4Address
import re
import json
from pvi import Connection, Device, Cpu, Task, Variable
from pvi.plcwatch_modules.resources import image_files


class TreeViewTooltip:
    def __init__(self, treeview):
        self.treeview = treeview
        self.tip_window = None
        self.item_tooltips = {}
        self.treeview.bind("<Motion>", self.on_motion)
        self.treeview.bind("<Leave>", self.hide_tooltip)

    def set_tooltip(self, item_id, tooltip_text):
        self.item_tooltips[item_id] = tooltip_text

    def on_motion(self, event):
        item = self.treeview.identify('item', event.x, event.y)
        if item and item in self.item_tooltips:
            self.show_tooltip(event, self.item_tooltips[item])
        else:
            self.hide_tooltip()

    def show_tooltip(self, event, text):
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = tk.Toplevel(self.treeview)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(self.tip_window, text=text, background="lightyellow",
                        relief=tk.SOLID, borderwidth=1)
        label.pack(ipadx=3, ipady=3)

    def hide_tooltip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None



class ObjectTreeView(ttk.Treeview):
    def __init__(self, parent : tk.Tk, pvi_connection : Connection, callback_ip_connected : Callable[[str],None] ):
        super().__init__( parent, columns=('name', 'value'), selectmode='browse' )
        self.tooltip_handler = TreeViewTooltip(self)
        self.pvi_connection = pvi_connection        
        self.callback_ip_connected = callback_ip_connected        
        self.image_storage = { str(k) : tk.PhotoImage( file = v ) for k,v in image_files.items() }        
        
        # # Create TreeView with scrollbar
        # tree_scroll = tk.Scrollbar(parent)
        # self.yscrollcommand=tree_scroll.set
        # tree_scroll.config(command=self.yview)
        # # Note: scrollbar added after tree to maintain proper z-order
        # self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)        
        
        # Add sample data to TreeView
        self.heading('#0', text='Name')
        self.heading('#1', text='Type')        
        self.heading('#2', text='Value')
        self.bind('<<TreeviewSelect>>', self.onItemSelected)
        self.bind("<<TreeviewOpen>>", self.onItemOpened )
        self.bind("<<TreeviewClose>>", self.onItemClosed)                
        self.cpu_list : List[Cpu] = []
        self.watch_list = dict()
        
        
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

            try:
                icon = self.image_storage[element.dataType]
            except KeyError:
                icon = self.image_storage['variable']
            except Exception as e:
                print( e )
                pass

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
        try:
            icon = self.image_storage[array.dataType.split('[')[0]]
        except KeyError:
            icon = self.image_storage['variable']
            pass        
        
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
                try:
                    icon = self.image_storage[variable.dataType]
                except KeyError:
                    icon = self.image_storage['variable']
                    pass
                
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
            parent = self.insert('', index = 'end', iid = iid, text=cpu.objectName, 
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
        cpu = Cpu( device, name, CD=f"/IP={ip.compressed} /SDT=5 /PVROI=1 /COMT=5000" )
        setattr( cpu, 'ip', ip.compressed )
        cpu.errorChanged = self.cpuErrorChanged
        
   
        
