from model import Model
from view import View
from config import *
import threading
from functions import *
import time

class Controller():
    def __init__(self):

        self.base_coin = 'USDT'
        self.base_coin_balance = ''
        self.equity = '900.0'

        self.position_size_percent_min = POSITION_SIZE_MIN
        self.position_size_percent_max = POSITION_SIZE_MAX
        self.rr_ratio_min = RR_RATIO_MIN
        self.rr_ratio_max = RR_RATIO_MAX
        self.risk_min = RISK_MIN
        self.risk_max = RISK_MAX
        self.entry_price = ENTRY_PRICE
        self.k = ADJUSTMENT_CONSTANT
        self.tick_size = TICK_SIZE
        self.lot_size = LOT_SIZE
        self.pair_list = get_available_pairs(base_coin)

        self.task_list = []
        self.new_task = None
        self.accept_new_task = True
    
        self.view = View(self.risk_min, self.risk_max, self.tick_size, self.pair_list)
        self.model = Model("model/tasks.db")
        threading.Thread(target=self.main_loop).start()

        self.view.run()
    
    def main_loop(self):
        while True:
            self.view_hanlder()
            self.model_handler()

    def view_hanlder(self):
        risk_percent_val = self.view.risk_percent_val
        take_profit_val = self.view.take_profit_val
        stop_loss_val = self.view.stop_loss_val
        entry_price_val = self.view.entry_price_val
        k = self.k
        position_size_val = get_position_size(stop_loss_val, entry_price_val, risk_percent_val, k)
        reward_percent_val = get_reward_percentage(take_profit_val, entry_price_val, position_size_val, k)

        self.view.stop_loss_min, self.view.stop_loss_max = self.get_stop_loss_range()
        self.view.position_size_val = position_size_val
        self.view.take_profit_min, self.view.take_profit_max = self.get_take_profit_range()
        self.view.rr_ratio_val = get_rr_ratio(reward_percent_val, risk_percent_val)
        self.view.accept_new_task = self.accept_new_task
        self.view.update_gui()
        self.view.get_user_input()

        self.event_monitor()

    def model_handler(self):
        # add new task on database
        if self.new_task:
            self.model.add_new_task(self.new_task)
            print("New task is added on database")
            self.new_task = None
            self.accept_new_task = True
            x = self.model.get_all_pending_tasks()
            print(x[-1].task_info)

        # get all pending tasks for exection from database
        self.task_list = self.model.get_all_pending_tasks()
        
        # execute pending tasks and update database
        for task in self.task_list:
            pass
            # new_task_details = execute_task(task)
            # self.model.update_task(new_task_details)        

    def get_stop_loss_range(self):
        risk_percent_val = self.view.risk_percent_val
        position_size_percent_min = self.position_size_percent_min
        position_size_percent_max = self.position_size_percent_max
        entry_price_val = self.view.entry_price_val
        k = self.k

        stop_loss_max = get_stop_loss(risk_percent_val, position_size_percent_max, entry_price_val, k)
        stop_loss_min = get_stop_loss(risk_percent_val, position_size_percent_min, entry_price_val, k)

        return stop_loss_min, stop_loss_max

    def get_take_profit_range(self):
        risk_percent_val = self.view.risk_percent_val
        rr_ratio_min = self.rr_ratio_min
        rr_ratio_max = self.rr_ratio_max
        position_size_val = self.view.position_size_val
        entry_price_val = self.view.entry_price_val
        k = self.k

        reward_min = get_reward(rr_ratio_min, risk_percent_val)
        reward_max = get_reward(rr_ratio_max, risk_percent_val)
        take_profit_min = get_take_profit(reward_min, position_size_val, entry_price_val, k)
        take_profit_max = get_take_profit(reward_max, position_size_val, entry_price_val, k)

        return take_profit_min, take_profit_max
    
    def event_monitor(self):
        if self.view.execute_button_pressed:
            self.accept_new_task = False
            self.new_task = Task()

            equity = get_equity(self.base_coin)
            if equity:
                self.equity = equity
                
            self.new_task.set_pair(self.view.pair)
            self.new_task.set_risk(self.get_risk())
            self.new_task.set_reward(self.get_reward())
            self.new_task.set_position_size(self.get_position_size())
            self.new_task.set_buy_price(self.get_buy_price())

            self.new_task.set_task_to_active()
            self.new_task.set_next_step('BUY')
            self.view.execute_button_pressed = False

    def get_risk(self):
        risk_percent = self.view.risk_percent_val
        return get_product(self.equity, risk_percent)

    def get_reward(self):
        risk_percent = self.view.risk_percent_val
        rr_ratio = self.view.rr_ratio_val
        return get_product(self.equity, risk_percent, rr_ratio)

    def get_position_size(self):
        pos_size_percent = self.view.position_size_val
        return get_product(self.equity, pos_size_percent)

    def get_buy_price(self):
        return self.view.entry_price_val
