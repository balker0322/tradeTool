import tkinter as tk

class TradeControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        width = 500

        # trade options
        frame1 = tk.Frame(self)
        trade_option_frame = tk.LabelFrame(frame1, text="Options", width=width)
        trade_option_frame.pack(fill=tk.Y, expand=1)


        # trade summary
        frame2 = tk.Frame(self)
        trade_summary_frame = tk.LabelFrame(frame2, text="Summary", width=width)
        trade_summary_frame.pack(fill=tk.Y, expand=1)

        frame1.pack(fill=tk.Y, expand=1, padx=10, pady=10)
        frame2.pack(fill=tk.Y, expand=1, padx=10, pady=10)

