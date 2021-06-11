import tkinter as tk
from .components import EntryComponent_A
from .components import EntryComponent_C
from .components import Container_A

from random import randint, random


def dummy_func():
    print(random())

class TradeEntry(tk.Frame):

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        container = Container_A(self, text='Trade Entry')
        container.pack(fill=tk.BOTH)

        self.market_entry = MarketEntry(container)
        self.market_entry.pack(fill=tk.BOTH)

        self.limit_price = LimitPrice(container)
        self.limit_price.pack(fill=tk.BOTH)

        self.limit_entry = LimitEntry(container)
        self.limit_entry.pack(fill=tk.BOTH)

        self.stop_liimt_entry = StopLimitEntry(container)
        self.stop_liimt_entry.pack(fill=tk.BOTH)

        dummy_label = tk.Label(self, text='')
        dummy_label.pack(fill=tk.X)


class MarketEntry(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_C(
            parent=self,
            label='Market Entry',
            entry_on_change=dummy_func,
            button_list=[
                {
                    'text':'LONG',
                    'command':dummy_func
                },
                {
                    'text':'SHORT',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)


class LimitPrice(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_A(
            parent=self,
            label='Limit / Stop Limit Price',
            entry_on_change=dummy_func,
            submit_button={
                'text':'Submit',
                'command':dummy_func
            },
        )
        self.target_entry.pack(fill=tk.BOTH)


class LimitEntry(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_C(
            parent=self,
            label='Limit Entry',
            entry_on_change=dummy_func,
            button_list=[
                {
                    'text':'LONG',
                    'command':dummy_func
                },
                {
                    'text':'SHORT',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)


class StopLimitEntry(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.target_entry = EntryComponent_C(
            parent=self,
            label='Stop Limit Entry',
            entry_on_change=dummy_func,
            button_list=[
                {
                    'text':'LONG',
                    'command':dummy_func
                },
                {
                    'text':'SHORT',
                    'command':dummy_func
                },
            ]
        )
        self.target_entry.pack(fill=tk.BOTH)