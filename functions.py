from decimal import Decimal as d
from model import Task
from copy import deepcopy
from binance_functions import *

def get_position_size(stop_loss, entry_price, risk_percentage, k = d("1.002")):
    position_size = d(risk_percentage) / (d("1.00") - (d(stop_loss) / (d(entry_price)*d(k))))
    return str(position_size)

def get_reward_percentage(take_profit, entry_price, position_size, k = d("1.002")):
    reward_percentage = d(position_size) * ( (d(take_profit) / (d(entry_price)*d(k))) - d("1.00") )
    return str(reward_percentage)

def get_reward(rr_ratio, risk):
    reward = d(rr_ratio) * d(risk)
    return str(reward)

def get_rr_ratio(reward, risk):
    rr_ratio = d(reward) / d(risk)
    return str(rr_ratio)

def get_stop_loss(risk, position_size, entry_price, k):
    stop_loss = d(k) * d(entry_price) * (d("1.00") - (d(risk)/d(position_size)))
    return str(stop_loss)

def get_take_profit(reward, position_size, entry_price, k):
    take_profit = d(k) * d(entry_price) * (d("1.00") + (d(reward)/d(position_size)))
    return str(take_profit)

def dec_to_percent_disp(dec_num):
    return "{0:.2f} %".format(d(dec_num)*d("100.00"))

def execute_task(task : Task):
    task = deepcopy(task)
    status = task.status

    if status == 'BUY':
        # symbol = task.symbol
        # quantity = task.quantity
        # response = market_buy_order(symbol, quantity)
        # if response:
        #     if response['buy_status'] == 'FILLED':
        #         task.status = 'GET_BUY_ORDER_STATUS'
        #         task.actual_buy_price = response['actual_buy_price']
        #         task.actual_buy_quantity = response['actual_buy_quantity']
        pass

    if status == 'GET_BUY_ORDER_STATUS':
        pass

    if status == 'SELL':
        pass

    if status == 'GET_BUY_SELL_STATUS':
        pass

    if status == 'DONE':
        pass

    if status == 'CANCELLED':
        pass  

    return task