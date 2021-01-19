import tkinter as tk

class Chart(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.label = tk.Button(self, text="Chart", bg="blue")
        self.label.pack(fill=tk.BOTH, expand=1)