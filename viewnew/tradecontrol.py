import tkinter as tk
import tkinter.ttk as ttk

tradeControlWidth = 40
valueColumnWidth = 20
labelColumnWidth = 12

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

        label_frame = tk.LabelFrame(self, text="Options")
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
        entry_price_var = tk.StringVar()
        entry_price_frame = tk.Frame(label_frame)
        entry_price_label = ttk.Label(entry_price_frame, text="Entry Price:", width=labelColumnWidth)
        entry_price_entry = tk.Entry(entry_price_frame, textvariable=entry_price_var)
        entry_price_label.pack(side=tk.LEFT, anchor=tk.S)
        entry_price_entry.pack(fill=tk.X)

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

        pair_frame.pack(fill=tk.X, padx=3, pady=3)
        risk_frame.pack(fill=tk.X, padx=3, pady=3)
        entry_price_frame.pack(fill=tk.X, padx=3, pady=3)
        stop_loss_frame.pack(fill=tk.X, padx=3, pady=3)
        take_profit_frame.pack(fill=tk.X, padx=3, pady=10)

        # dummy label for sizing
        dummy_label = ttk.Label(label_frame, text="", width=tradeControlWidth)
        dummy_label.pack()


class TradeSummary(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        label_frame = tk.LabelFrame(self, text="Trade Summary")
        label_frame.pack(fill=tk.Y, expand=1)

        # entry price
        entry_price_val = "entry_price sample"
        entry_price_frame = tk.Frame(label_frame)
        entry_price_label = ttk.Label(entry_price_frame, text="Entry Price:", width=labelColumnWidth)
        entry_price_label.pack(side=tk.LEFT)
        entry_price_disp = ttk.Label(entry_price_frame, text=entry_price_val, width=valueColumnWidth)
        entry_price_disp.pack(fill=tk.X)

        # stop loss
        stop_loss_val = "stop_loss sample"
        stop_loss_frame = tk.Frame(label_frame)
        stop_loss_label = ttk.Label(stop_loss_frame, text="Stop Loss:", width=labelColumnWidth)
        stop_loss_label.pack(side=tk.LEFT)
        stop_loss_disp = ttk.Label(stop_loss_frame, text=stop_loss_val, width=valueColumnWidth)
        stop_loss_disp.pack(fill=tk.X)

        # take profit
        take_profit_val = "take_profit sample"
        take_profit_frame = tk.Frame(label_frame)
        take_profit_label = ttk.Label(take_profit_frame, text="Take Profit:", width=labelColumnWidth)
        take_profit_label.pack(side=tk.LEFT)
        take_profit_disp = ttk.Label(take_profit_frame, text=take_profit_val, width=valueColumnWidth)
        take_profit_disp.pack(fill=tk.X)

        # risk
        risk_val = "risk sample"
        risk_frame = tk.Frame(label_frame)
        risk_label = ttk.Label(risk_frame, text="Risk:", width=labelColumnWidth)
        risk_label.pack(side=tk.LEFT)
        risk_disp = ttk.Label(risk_frame, text=risk_val, width=valueColumnWidth)
        risk_disp.pack(fill=tk.X, expand=1)

        # rr ratio
        rr_ratio_val = "rr_ratio sample"
        rr_ratio_frame = tk.Frame(label_frame)
        rr_ratio_label = ttk.Label(rr_ratio_frame, text="RR Ratio:", width=labelColumnWidth)
        rr_ratio_label.pack(side=tk.LEFT)
        rr_ratio_disp = ttk.Label(rr_ratio_frame, text=rr_ratio_val, width=valueColumnWidth)
        rr_ratio_disp.pack(fill=tk.X)

        # position size
        postion_size_val = "postion_size sample"
        postion_size_frame = tk.Frame(label_frame)
        postion_size_label = ttk.Label(postion_size_frame, text="Position Size:", width=labelColumnWidth)
        postion_size_label.pack(side=tk.LEFT)
        postion_size_disp = ttk.Label(postion_size_frame, text=postion_size_val, width=valueColumnWidth)
        postion_size_disp.pack(fill=tk.X)
    
        entry_price_frame.pack(fill=tk.X, padx=3, pady=3)
        stop_loss_frame.pack(fill=tk.X, padx=3, pady=3)
        take_profit_frame.pack(fill=tk.X, padx=3, pady=3)
        risk_frame.pack(fill=tk.X, padx=3, pady=3)
        rr_ratio_frame.pack(fill=tk.X, padx=3, pady=3)
        postion_size_frame.pack(fill=tk.X, padx=3, pady=3)

        # dummy label for sizing
        dummy_label = ttk.Label(label_frame, text="", width=tradeControlWidth)
        dummy_label.pack()