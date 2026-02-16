import tkinter as tk
from tkinter import ttk

class ObjectTreeView(ttk.Treeview):
    def __init__(self, parent : tk.PanedWindow ):
        super().__init__()
        # Create TreeView with scrollbar
        tree_scroll = tk.Scrollbar(parent)
        
        self.tree = ttk.Treeview(parent, yscrollcommand=tree_scroll.set)
        parent.add(self.tree, minsize=150)
        
        tree_scroll.config(command=self.tree.yview)
        # Note: scrollbar added after tree to maintain proper z-order
        
        # Add sample data to TreeView
        self.tree.heading('#0', text='Tree View')
        parent1 = self.tree.insert('', 'end', text='Parent 1')
        self.tree.insert(parent1, 'end', text='Child 1.1')
        self.tree.insert(parent1, 'end', text='Child 1.2')
        parent2 = self.tree.insert('', 'end', text='Parent 2')
        self.tree.insert(parent2, 'end', text='Child 2.1')
        