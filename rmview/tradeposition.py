import tkinter as tk
from .components import EntryComponent_A
from .components import EntryComponent_B
from .components import Container_A
from random import randint, random


def dummy_func():
    print(random())

class TradePosition(tk.Frame):

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        container = Container_A(self, text='Position Sizing')
        container.pack(fill=tk.BOTH)

        self.capital = Capital(container)
        self.capital.pack(fill=tk.BOTH)

        self.target_entry = TargetEntry(container)
        self.target_entry.pack(fill=tk.BOTH)

        self.target_exit = TargetExit(container)
        self.target_exit.pack(fill=tk.BOTH)

        self.risk = Risk(container)
        self.risk.pack(fill=tk.BOTH)

        self.position_size = PositionSize(container)
        self.position_size.pack(fill=tk.BOTH)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)



class Capital(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_A(
            parent=self,
            label='Capital',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
        )
        self.target_entry.pack(fill=tk.BOTH)



class TargetEntry(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='Target Entry Price',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'--',
                    'command':dummy_func
                },
                {
                    'text':'-',
                    'command':dummy_func
                },
                {
                    'text':'Market Price',
                    'command':dummy_func
                },
                {
                    'text':'+',
                    'command':dummy_func
                },
                {
                    'text':'++',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)


class TargetExit(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='Target Exit Price',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'--',
                    'command':dummy_func
                },
                {
                    'text':'-',
                    'command':dummy_func
                },
                {
                    'text':'Market Price',
                    'command':dummy_func
                },
                {
                    'text':'+',
                    'command':dummy_func
                },
                {
                    'text':'++',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)


class Risk(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='Risk',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'-2.00%',
                    'command':dummy_func
                },
                {
                    'text':'-1.75%',
                    'command':dummy_func
                },
                {
                    'text':'-1.50%',
                    'command':dummy_func
                },
                {
                    'text':'-1.25%',
                    'command':dummy_func
                },
                {
                    'text':'-1.00%',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)


class PositionSize(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='Position Size',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'20%',
                    'command':dummy_func
                },
                {
                    'text':'40%',
                    'command':dummy_func
                },
                {
                    'text':'60%',
                    'command':dummy_func
                },
                {
                    'text':'80%',
                    'command':dummy_func
                },
                {
                    'text':'100%',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)