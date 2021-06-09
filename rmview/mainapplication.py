import tkinter as tk
from .components import EntryComponent

def dummy_func():
    pass

class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()

        # self.geometry("1500x900")

        self.sample_comp = EntryComponent(
            parent=self,
            label='sample label',
            entry_on_change=dummy_func,
            submit_button={
                'text':'submit',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'button1',
                    'command':self.set_variable
                },
                {
                    'text':'button2',
                    'command':dummy_func
                },
                {
                    'text':'button3',
                    'command':dummy_func
                },
                {
                    'text':'button4',
                    'command':dummy_func
                },
                {
                    'text':'button5',
                    'command':dummy_func
                },
            ]
        )
        self.sample_comp.pack(fill=tk.BOTH)

    def set_variable(self):
        self.sample_comp.set_entry('hello')