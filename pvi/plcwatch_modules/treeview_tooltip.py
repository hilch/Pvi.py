import tkinter as tk
from tkinter import ttk

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