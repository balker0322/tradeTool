import tkinter as tk

class TradeLog(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.label = tk.Button(self, text="log", bg="green")
        self.label.pack(fill=tk.BOTH, expand=1)