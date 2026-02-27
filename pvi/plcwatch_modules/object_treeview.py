import tkinter as tk
from tkinter import ttk
from collections import OrderedDict 
from typing import List, Any
from ipaddress import IPv4Address
import re
from pvi_objects.include import T_POBJ_TYPE
from pvi import Connection, PviObject, Line, Device, Cpu, Task, Variable
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
    def __init__(self, parent : tk.Tk, pvi_connection : Connection ):
        super().__init__( parent, columns=('name', 'value'), selectmode='browse' )
        self.tooltip_handler = TreeViewTooltip(self)
        self.pvi_connection = pvi_connection        
        self.image_storage = { str(k) : tk.PhotoImage( file = v ) for k,v in image_files.items() }        
        
        # Create TreeView with scrollbar
        tree_scroll = tk.Scrollbar(parent)
        
        #self.tree = ttk.Treeview(parent, yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=self.yview)
        # Note: scrollbar added after tree to maintain proper z-order
        
        # Add sample data to TreeView
        self.heading('#0', text='Name')
        self.heading('#1', text='Value')
        self.bind('<<TreeviewSelect>>', self.onItemSelected)
        # parent1 = self.insert('', 'end', text='Parent 1', image=self.image_storage['cpu'])
        # self.insert(parent1, 'end', text='Child 1.1', image=self.image_storage['task'])
        # self.insert(parent1, 'end', text='Child 1.2')
        # parent2 = self.insert('', 'end', text='Parent 2')
        # self.insert(parent2, 'end', text='Child 2.1')
        
        self.cpu_list : List[Cpu] = []
        
        
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

            if element.isArray:
                ##array_variable = Variable( task, struct.objectName + element_name)
                # insert array variable itself
                self.insert( struct.name, index = 'end', 
                                iid = element.name, text = element_name,
                            image = self.image_storage['array'] ) 
                self.tooltip_handler.set_tooltip(struct.name, struct.name)   
                # insert array elements
                self.expandArray( task, element )
                #array_variable.kill()                
            elif isinstance(element.value, OrderedDict):
                ##substructure = Variable( task, struct.objectName + element_name )
                # insert the substructure itself
                self.insert( struct.name, index = 'end', 
                                         iid = element.name, text = element_name,
                            image = self.image_storage['struct'] ) 
                self.tooltip_handler.set_tooltip(struct.name, struct.name)   
                self.expandStruct(task, element)           
                #substructure.kill()
            else:       
                self.insert( struct.name, index = 'end', iid = element.name, text = element_name,
                                image = icon, values = (element.value,) )  
                self.tooltip_handler.set_tooltip(struct.name, struct.name)  
            #element.kill()
        
        
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
                    if isinstance( vk, OrderedDict ):
                        #insert struct itself
                        self.insert( array.name, index = 'end', 
                            iid = f'{array.name}[{i1},{i2}]', text = f'[{i1},{i2}]',
                            image = self.image_storage['struct'] )
                        self.tooltip_handler.set_tooltip(array.name, array.name)
                        struct = Variable( task, f'{array.objectName}[{i1},{i2}]' )
                        self.expandStruct( task, struct )
                    else:
                        self.insert( array.name, index = 'end', 
                                iid = f'{array.name}[{i1},{i2}]', text = f'[{i1},{i2}]',
                                image = icon, values = vk )
                        self.tooltip_handler.set_tooltip(array.name, array.name)
            else: # vector
                i1 = indices[0][0] + j
                if isinstance( v, OrderedDict):
                    #insert struct itself
                    self.insert( array.name, index = 'end', 
                        iid = f'{array.name}[{i1}]', text = f'[{i1}]',
                        image = self.image_storage['struct'] )
                    self.tooltip_handler.set_tooltip(array.name, array.name)
                    struct = Variable( task, f'{array.objectName}[{i1}]' )
                    self.expandStruct( task, struct )
                else:
                    self.insert( array.name, index = 'end', 
                            iid = f'{array.name}[{i1}]', text = f'[{i1}]',
                            image = icon, values = v )
                    self.tooltip_handler.set_tooltip(array.name, array.name)
        
        
    def onTaskClicked( self, item : str, task : Task ):
        if not self.get_children(item):
            variableNames = [ _['name'] for _ in task.externalObjects]
            for name in variableNames:
                variable = Variable(task, name)
                try:
                    icon = self.image_storage[variable.dataType]
                except KeyError:
                    icon = self.image_storage['variable']
                    pass
                
                value = variable.value
                if isinstance(value, list ): # is variable an array ?
                    # insert array itself
                    self.insert( item, index = 'end', iid = variable.name, text = name,
                                image = self.image_storage['array'] )
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                    self.expandArray(task,variable)                
                elif isinstance(value, OrderedDict): # is variable a struct ?
                    # insert struct itself
                    self.insert( item, index = 'end', iid = variable.name, text = name,
                                image = self.image_storage['struct'] )    
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                    # insert children
                    self.expandStruct(task, variable)
                else: # variable with basic datatype        
                    self.insert( item, index = 'end', iid = variable.name, text = name,
                                image = icon, values = (value,) )    
                    self.tooltip_handler.set_tooltip(variable.name, variable.name)
                
        
    def onItemSelected( self, event ):
        # Change cursor to hourglass/watch during execution
        self.config(cursor="watch")
        self.update_idletasks()  # Force cursor update
        
        try:
            item  = self.selection()[0]
            try:
                object : PviObject = self.pvi_connection.findObjectByName(item)
                if object.type == T_POBJ_TYPE.POBJ_TASK:
                    self.onTaskClicked( item, object ) # type: ignore
            except KeyError:
                pass
        finally:
            # Restore cursor to default
            self.config(cursor="")
            self.update_idletasks()
        
        
    def cpuErrorChanged( self, cpu : Cpu,  error : int ):
        if error == 11020:
            print("Unable to establish connection")
        elif error != 0:
            pass
        else:
            values = cpu.cpuInfo.get('CT', 'unknown') + '/' + cpu.status.get('RunState','unknown')
            self.cpu_list.append(cpu)
            parent = self.insert('', index = 'end', iid = cpu.name, text=cpu.objectName, 
                        image=self.image_storage['cpu'], values = values)
            self.tooltip_handler.set_tooltip(cpu.name, cpu.name)
            allObjects = cpu.externalObjects
            # read task names
            taskNames = [ _['name'] for _ in allObjects if _['type'] == 'Task'] 
            for name in taskNames:  # read the tasks' status
                task = Task( cpu, name.replace('::','__'), CD=f'"{name}"' )
                values = task.status['ST']
                self.insert( parent, index = 'end', iid = task.name, text = name,
                            image = self.image_storage['task'], values = values )    
                self.tooltip_handler.set_tooltip(task.name, task.name)
    
        
    def insert_cpu(self, device : Device, ip : IPv4Address ):
        name = ip.compressed.replace('.','_')
        cpu = Cpu( device, name, CD=f"/IP={ip.compressed} /SDT=5 /PVROI=1 /COMT=5000" )
        cpu.errorChanged = self.cpuErrorChanged
        
        
        