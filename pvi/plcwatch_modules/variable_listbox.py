import tkinter as tk
from tkinter import ttk


class VariableListBox(ttk.Treeview):
    def __init__(self, parent : tk.PanedWindow ):
        super().__init__()
        # Create Treeview with columns for multi-column listbox
        list_scroll = tk.Scrollbar(parent)
        
        # Define columns
        self.listbox = ttk.Treeview(parent, columns=('Name', 'Type', 'Value'), 
                                     show='headings', yscrollcommand=list_scroll.set)
        parent.add(self.listbox, minsize=150)
        
        list_scroll.config(command=self.listbox.yview)
        
        # Configure column headings
        self.listbox.heading('Name', text='Name')
        self.listbox.heading('Type', text='Type')
        self.listbox.heading('Value', text='Value')
        
        # Configure column widths
        self.listbox.column('Name', width=150, anchor='w')
        self.listbox.column('Type', width=100, anchor='center')
        self.listbox.column('Value', width=150, anchor='w')
        
        # Add sample data to multi-column listbox
        sample_data = [
            ('Variable_1', 'INT', '100'),
            ('Variable_2', 'BOOL', 'TRUE'),
            ('Variable_3', 'REAL', '3.14'),
            ('Temperature', 'REAL', '25.5'),
            ('Pressure', 'INT', '1013'),
            ('Status', 'BOOL', 'FALSE'),
            ('Counter', 'DINT', '12345'),
            ('Timer', 'TIME', '1000ms'),
            ('Speed', 'REAL', '45.8'),
            ('Position', 'INT', '500'),
            ('Alarm', 'BOOL', 'TRUE'),
            ('SetPoint', 'REAL', '100.0'),
            ('Output', 'INT', '75'),
            ('Input', 'INT', '50'),
            ('Mode', 'STRING', 'AUTO'),
        ]
        
        for item in sample_data:
            self.listbox.insert('', 'end', values=item)