from .widgets import *


class View():
    def __init__(self, risk_percent_min, risk_percent_max, tick_size):
        self.risk_percent_min = risk_percent_min
        self.risk_percent_max = risk_percent_max
        self.tick_size = tick_size

        self.execute_button_pressed = False

        self.position_size_val = "1.0"
        self.risk_percent_val = "0.02"
        self.rr_ratio_val = "2.0"
        self.entry_price_val = "20000"
        self.stop_loss_val = "0"
        self.take_profit_val = "0"
        self.stop_loss_min = "0"
        self.stop_loss_max = "0"
        self.take_profit_min = "0"
        self.take_profit_max = "0"

        self.root = Tk()
        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        # frame for user input
        self.option_frame = LabelFrame(self.main_frame, text="Options")
        self.option_frame.pack(fill=X)
        self.risk_input = slider_input(master=self.option_frame, label = "Risk Percentage:")
        self.risk_input.scale.config(from_=float(self.risk_percent_min), to=float(self.risk_percent_max), resolution=.0001, showvalue=0)
        self.entry_price_input = entry(master=self.option_frame, label = "Entry Price:")
        self.entry_price_input.var.set("19000")
        self.stop_loss_input = slider_input(master=self.option_frame, label = "Stop Loss:")
        self.stop_loss_input.scale.config(resolution=float(self.tick_size))
        self.take_profit_input = slider_input(master=self.option_frame, label = "Take Profit:")
        self.take_profit_input.scale.config(resolution=float(self.tick_size))

        # frame for summary of trading parameters
        self.summary_frame = LabelFrame(self.main_frame, text="Trade Summary")
        self.summary_frame.pack(fill=X)
        self.entry_price_diplay = display_value(master=self.summary_frame, label="Entry Price:", value="100")
        self.stop_loss_display = display_value(master=self.summary_frame, label="Stop Loss:", value="100")
        self.take_profit_display = display_value(master=self.summary_frame, label="Take Profit:", value="100")
        self.risk_percentage_diplay = display_value(master=self.summary_frame, label="Risk Percentage:", value="100")
        self.rr_ratio_diplay = display_value(master=self.summary_frame, label="RR ratio:", value="100")
        self.position_size_diplay = display_value(master=self.summary_frame, label="Position Size Percent:", value="100")

        # frame for trade execution buttons
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(fill=X)
        self.execute_button = Button(self.button_frame, text = "Execute", command = self.execute_trade)
        self.execute_button.pack(anchor = CENTER)

        self.accept_new_task = True


    def update_gui(self):
        self.stop_loss_input.scale.config(from_=float(self.stop_loss_min), to=float(self.stop_loss_max))
        self.take_profit_input.scale.config(from_=float(self.take_profit_min), to=float(self.take_profit_max))
        if self.accept_new_task:
            self.execute_button['state'] = NORMAL
        self.update_display_summary()
    
    def update_display_summary(self):
        self.position_size_diplay.update(self.dec_to_percent_disp(self.position_size_val))
        self.risk_percentage_diplay.update(self.dec_to_percent_disp(self.risk_percent_val))
        self.rr_ratio_diplay.update("{0:.4f}".format(float(self.rr_ratio_val)))
        self.entry_price_diplay.update(self.entry_price_val)
        self.stop_loss_display.update(self.stop_loss_val)
        self.take_profit_display.update(self.take_profit_val)
    
    def get_user_input(self):
        self.risk_percent_val =str(self.risk_input.var.get())
        entry_price_str = str(self.entry_price_input.var.get())
        try:
            self.entry_price_val = str(float(entry_price_str))
        except:
            pass
        self.stop_loss_val = str(self.stop_loss_input.var.get())
        self.take_profit_val = str(self.take_profit_input.var.get())

    def add_task(self):
        pass

    def execute_trade(self):
        self.execute_button_pressed = True
        trade_options = dict()
        trade_options['risk_percent_val'] = self.risk_percent_val
        trade_options['take_profit_val'] = self.take_profit_val
        trade_options['stop_loss_val'] = self.stop_loss_val
        trade_options['entry_price_val'] = self.entry_price_val
        trade_options['position_size_val'] = self.position_size_val
        trade_options['take_profit_min'] = self.take_profit_min
        trade_options['rr_ratio_val'] = self.rr_ratio_val
        self.trade_options = trade_options

        # disable execute button
        self.execute_button['state'] = DISABLED
    
    def run(self):
        self.root.mainloop()

    def dec_to_percent_disp(self, dec_num):
        return "{0:.2f} %".format(float(dec_num)*float("100.00"))