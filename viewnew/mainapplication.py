import tkinter as tk
from .chart import Chart
from .tradecontrol import TradeControl
from .tradelog import TradeLog 


class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("1500x900")

        frame1 = tk.Frame(self)
        self.trade_control = TradeControl(frame1)
        self.chart = Chart(frame1)
        self.trade_log = TradeLog(self)

        frame1.pack(fill=tk.BOTH, expand=1)
        self.trade_control.pack(side=tk.RIGHT, fill=tk.Y)
        self.chart.pack(fill=tk.BOTH, expand=1)
        self.trade_log.pack(fill=tk.X)
        
