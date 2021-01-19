import tkinter as tk

tradeControlWidth = 500

class TradeControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        trade_option_frame = TradeOptions(self)
        trade_summary_frame = TradeSummary(self)

        trade_option_frame.pack(fill=tk.Y, expand=1, padx=10, pady=10)
        trade_summary_frame.pack(fill=tk.Y, expand=1, padx=10, pady=10)


class TradeOptions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label_frame = tk.LabelFrame(self, text="Options", width=tradeControlWidth)
        label_frame.pack(fill=tk.Y, expand=1)


class TradeSummary(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label_frame = tk.LabelFrame(self, text="Summary", width=tradeControlWidth)
        label_frame.pack(fill=tk.Y, expand=1)