import tkinter as tk
import tkinter.ttk as ttk
from .tradeentry import TradeEntry
from .tradeexit import TradeExit
from .tradeposition import TradePosition
from .components import VerticalScrolledFrame


class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()

        # self.geometry("1500x900")

        container = self

        self.trade_position = TradePosition(container)
        self.trade_position.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.trade_entry = TradeEntry(container)
        self.trade_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.trade_exit = TradeExit(container)
        self.trade_exit.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # def set_variable(self):
    #     self.sample_comp.set_entry('hello')