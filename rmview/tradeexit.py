import tkinter as tk
from .components import Container_A
from .components import EntryComponent_A
from .components import EntryComponent_B
from .components import EntryComponent_C
from .components import EntryComponent_D
from random import randint, random


def dummy_func():
    print(random())

class TradeExit(tk.Frame):

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        container = Container_A(self, text='Trade Exit')
        container.pack(fill=tk.BOTH)

        self.risk = Risk(container)
        self.risk.pack(fill=tk.BOTH)

        self.stop_loss = StopLoss(container)
        self.stop_loss.pack(fill=tk.BOTH)

        self.rrratio = RRratio(container)
        self.rrratio.pack(fill=tk.BOTH)

        self.take_profit = TakeProfit(container)
        self.take_profit.pack(fill=tk.BOTH)

        


class Risk(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='Risk',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Autoset SL',
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


class StopLoss(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_D(
            parent=self,
            label='Stop Loss',
            entry_on_change=dummy_func,
            button_list=[
                {
                    'text':'Cancel SL',
                    'command':dummy_func
                },
                {
                    'text':'Set SL',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)



class RRratio(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_B(
            parent=self,
            label='RR Ratio',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Autoset TP',
                'command':dummy_func
            },
            button_list=[
                {
                    'text':'1.00',
                    'command':dummy_func
                },
                {
                    'text':'1.50',
                    'command':dummy_func
                },
                {
                    'text':'2.00',
                    'command':dummy_func
                },
                {
                    'text':'2.50',
                    'command':dummy_func
                },
                {
                    'text':'3.00',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)



class TakeProfit(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_D(
            parent=self,
            label='Take Profit',
            entry_on_change=dummy_func,
            button_list=[
                {
                    'text':'Cancel TP',
                    'command':dummy_func
                },
                {
                    'text':'Set TP',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)
