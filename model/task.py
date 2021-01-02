

info_list = [
    "id",
    "pair",
    "quantity",
    "take_profit_val",
    "stop_loss_val",
    "entry_price_val",
    "position_size_val",
    "take_profit_min",
    "risk_percent_val",
    "status",
    "next_step",
    "timestamp",
]

class Task():
    def __init__(self, ):

        self.task_info = dict()

        for info in info_list:
            self.task_info[info] = ""
    
    def set_symbol(self, symbol):
        self.task_info["symbol"] = symbol

    def set_quantity(self, quantity):
        self.task_info["quantity"] = quantity

    def set_take_profit_val(self, take_profit_val):
        self.task_info["take_profit_val"] = take_profit_val

    def set_stop_loss_val(self, stop_loss_val):
        self.task_info["stop_loss_val"] = stop_loss_val

    def set_entry_price_val(self, entry_price_val):
        self.task_info["entry_price_val"] = entry_price_val

    def set_position_size_val(self, position_size_val):
        self.task_info["position_size_val"] = position_size_val

    def set_take_profit_min(self, take_profit_min):
        self.task_info["take_profit_min"] = take_profit_min

    def set_risk_percent_val(self, risk_percent_val):
        self.task_info["risk_percent_val"] = risk_percent_val

    def set_status(self, status):
        self.task_info["status"] = status

    def set_next_step(self, next_step):
        self.task_info["next_step"] = next_step

    def set_timestamp(self, timestamp):
        self.task_info["timestamp"] = timestamp
    
    def set_task_to_active(self):
        self.set_status('ACTIVE')
    
    def set_task_to_inactive(self):
        self.set_status('INACTIVE')


    def get_id(self):
        return self.task_info["id"]

    def get_symbol(self):
        return self.task_info["symbol"]

    def get_quantity(self):
        return self.task_info["quantity"]

    def get_take_profit_val(self):
        return self.task_info["take_profit_val"]

    def get_stop_loss_val(self):
        return self.task_info["stop_loss_val"]

    def get_entry_price_val(self):
        return self.task_info["entry_price_val"]

    def get_position_size_val(self):
        return self.task_info["position_size_val"]

    def get_take_profit_min(self):
        return self.task_info["take_profit_min"]

    def get_risk_percent_val(self):
        return self.task_info["risk_percent_val"]

    def get_status(self):
        return self.task_info["status"]

    def get_next_step(self):
        return self.task_info["next_step"]

    def get_timestamp(self):
        return self.task_info["timestamp"]

