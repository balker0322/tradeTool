import tkinter as tk
import tkinter.ttk as ttk

tradeControlWidth = 300
valueColumnWidth = 30
labelColumnWidth = 15

class TradeControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.trade_option_frame = TradeOptions(self)
        self.trade_summary_frame = TradeSummary(self)

        self.trade_option_frame.pack(fill=tk.Y, expand=1, padx=10, pady=10)
        self.trade_summary_frame.pack(fill=tk.Y, expand=1, padx=10, pady=10)


class TradeOptions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label_frame = tk.LabelFrame(self, text="Options", width=tradeControlWidth)
        label_frame.pack(fill=tk.Y, expand=1)

        # pair
        options = ['qwe', 'sdf', 'ghj'] # TODO
        pair_frame = tk.Frame(label_frame)
        pair_label = ttk.Label(pair_frame, text="Pair:", width=labelColumnWidth)
        pair_dropdown = ttk.Combobox(pair_frame, values = options, width=valueColumnWidth)
        pair_dropdown.current(0)
        pair_label.pack(side=tk.LEFT)
        pair_dropdown.pack(fill=tk.X)

        # risk percentage
        risk_var = tk.DoubleVar() # TODO
        risk_frame = tk.Frame(label_frame)
        risk_label = ttk.Label(risk_frame, text="Risk:", width=labelColumnWidth)
        risk_scale = tk.Scale(risk_frame, variable = risk_var, orient=tk.HORIZONTAL)
        risk_label.pack(side=tk.LEFT, anchor=tk.S)
        risk_scale.pack(fill=tk.X)

        # entry price
        entry_price_frame = tk.Frame(label_frame)

        # stop loss
        stop_loss_frame = tk.Frame(label_frame)
        stop_loss_var = tk.DoubleVar() # TODO
        stop_loss_frame = tk.Frame(label_frame)
        stop_loss_label = ttk.Label(stop_loss_frame, text="Stop Loss:", width=labelColumnWidth)
        stop_loss_scale = tk.Scale(stop_loss_frame, variable = stop_loss_var, orient=tk.HORIZONTAL)
        stop_loss_label.pack(side=tk.LEFT, anchor=tk.S)
        stop_loss_scale.pack(fill=tk.X)

        # take profit
        take_profit_frame = tk.Frame(label_frame)
        take_profit_var = tk.DoubleVar() # TODO
        take_profit_frame = tk.Frame(label_frame)
        take_profit_label = ttk.Label(take_profit_frame, text="Take Profit:", width=labelColumnWidth)
        take_profit_scale = tk.Scale(take_profit_frame, variable = take_profit_var, orient=tk.HORIZONTAL)
        take_profit_label.pack(side=tk.LEFT, anchor=tk.S)
        take_profit_scale.pack(fill=tk.X)

        pair_frame.pack(fill=tk.X)
        risk_frame.pack(fill=tk.X)
        entry_price_frame.pack(fill=tk.X)
        stop_loss_frame.pack(fill=tk.X)
        take_profit_frame.pack(fill=tk.X)


class TradeSummary(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label_frame = tk.LabelFrame(self, text="Trade Summary", width=tradeControlWidth)
        label_frame.pack(fill=tk.Y, expand=1)