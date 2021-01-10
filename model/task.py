import time

info_list = [
    "task_id",
    "create_task_timestamp",
    "end_task_timestamp",
    "reward",
    "pair",
    "buy_price",
    "sell_price",
    "position_size",
    "profit",
    "buy_order_id",
    "take_profit_order_id",
    "stop_loss_order_id",
    "status",
    "next_step",
]

class Task():
    def __init__(self, ):

        self.task_info = dict()

        for info in info_list:
            self.task_info[info] = ""
    

    def set_task_to_active(self):

        self.set_create_task_timestamp(
            self.__get_timestamp()
        )

        self.set_status('ACTIVE')


    def set_task_to_inactive(self):

        self.set_end_task_timestamp(
            self.__get_timestamp()
        )

        self.set_status('INACTIVE')

    
    def __get_timestamp(self):
        return str(int(round(time.time() * 1000)))

    def set_task_id(self, task_id):
        self.task_info['task_id'] = task_id
        
    def set_create_task_timestamp(self, create_task_timestamp):
        self.task_info['create_task_timestamp'] = create_task_timestamp
        
    def set_end_task_timestamp(self, end_task_timestamp):
        self.task_info['end_task_timestamp'] = end_task_timestamp
        
    def set_reward(self, reward):
        self.task_info['reward'] = reward
        
    def set_pair(self, pair):
        self.task_info['pair'] = pair
        
    def set_buy_price(self, buy_price):
        self.task_info['buy_price'] = buy_price
        
    def set_sell_price(self, sell_price):
        self.task_info['sell_price'] = sell_price
        
    def set_position_size(self, position_size):
        self.task_info['position_size'] = position_size
        
    def set_profit(self, profit):
        self.task_info['profit'] = profit
        
    def set_buy_order_id(self, buy_order_id):
        self.task_info['buy_order_id'] = buy_order_id
        
    def set_take_profit_order_id(self, take_profit_order_id):
        self.task_info['take_profit_order_id'] = take_profit_order_id
        
    def set_stop_loss_order_id(self, stop_loss_order_id):
        self.task_info['stop_loss_order_id'] = stop_loss_order_id
        
    def set_status(self, status):
        self.task_info['status'] = status
        
    def set_next_step(self, next_step):
        self.task_info['next_step'] = next_step

    def get_task_id(self):
        return self.task_info['task_id']

    def get_create_task_timestamp(self):
        return self.task_info['create_task_timestamp']

    def get_end_task_timestamp(self):
        return self.task_info['end_task_timestamp']

    def get_reward(self):
        return self.task_info['reward']

    def get_pair(self):
        return self.task_info['pair']

    def get_buy_price(self):
        return self.task_info['buy_price']

    def get_sell_price(self):
        return self.task_info['sell_price']

    def get_position_size(self):
        return self.task_info['position_size']

    def get_profit(self):
        return self.task_info['profit']

    def get_buy_order_id(self):
        return self.task_info['buy_order_id']

    def get_take_profit_order_id(self):
        return self.task_info['take_profit_order_id']

    def get_stop_loss_order_id(self):
        return self.task_info['stop_loss_order_id']

    def get_status(self):
        return self.task_info['status']

    def get_next_step(self):
        return self.task_info['next_step']






