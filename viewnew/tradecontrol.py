import tkinter as tk

class TradeControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.label = tk.Button(self, text="control", bg="red")
        self.label.pack(fill=tk.BOTH, expand=1)
