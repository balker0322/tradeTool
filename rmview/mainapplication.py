import tkinter as tk
from .components import EntryComponent

class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()

        # self.geometry("1500x900")

        sample_comp = EntryComponent(self)
        sample_comp.pack(fill=tk.BOTH)