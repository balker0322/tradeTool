from decimal import Decimal as d
from model import Task
from copy import deepcopy
from binance_api import *
import time
from config import ADJUSTMENT_CONSTANT, BASE_COIN

k = ADJUSTMENT_CONSTANT
base_coin = BASE_COIN

def get_position_size(stop_loss, entry_price, risk_percentage, k = k):
    position_size = d(risk_percentage) / (d("1.00") - (d(stop_loss) / (d(entry_price)*d(k))))
    return str(position_size)

def get_reward_percentage(take_profit, entry_price, position_size, k = k):
    reward_percentage = d(position_size) * ( (d(take_profit) / (d(entry_price)*d(k))) - d("1.00") )
    return str(reward_percentage)

def get_reward(rr_ratio, risk):
    reward = d(rr_ratio) * d(risk)
    return str(reward)

def get_rr_ratio(reward, risk):
    rr_ratio = d(reward) / d(risk)
    return str(rr_ratio)

def get_stop_loss(risk, position_size, entry_price, k = k):
    stop_loss = d(k) * d(entry_price) * (d("1.00") - (d(risk)/d(position_size)))
    return str(stop_loss)

def get_take_profit(reward, position_size, entry_price, k = k):
    take_profit = d(k) * d(entry_price) * (d("1.00") + (d(reward)/d(position_size)))
    return str(take_profit)

def dec_to_percent_disp(dec_num):
    return "{0:.2f} %".format(d(dec_num)*d("100.00"))

def get_available_pairs(base_symbol : str):
    return get_all_pairs(base_symbol)

def get_product(*args):
    product = d('1.0')
    for num in args:
        product *= d(num)
    return str(product)
        
def execute_task(task : Task):
    next_step = task.get_next_step()

    if next_step == 'BUY':
        return execute_buy(task)

    if next_step == 'GET_BUY_ORDER_STATUS':
        return execute_wait_buy(task)

    if next_step == 'SELL':
        return execute_sell(task)

    if next_step == 'GET_BUY_SELL_STATUS':
        return execute_wait_sell(task)

    if next_step == 'DONE':
        return execute_done(task)

    if next_step == 'CANCEL':
        return execute_cancel(task)


def execute_buy(task : Task):
    print('execute_buy...')
    task = deepcopy(task)
    
    symbol = task.get_pair()
    quantity = get_buy_quantity(symbol, task.get_position_size())
    price = task.get_buy_price()
    response = order_limit_buy(symbol, quantity, price)

    if response:
            
        buy_order_id  = response['orderId']
        task.set_buy_order_id(buy_order_id)

        next_step = 'GET_BUY_ORDER_STATUS'
        task.set_next_step(next_step)

        return task

    task.set_next_step('CANCEL')
    return task


def execute_wait_buy(task : Task):
    print('execute_wait_buy...')
    task = deepcopy(task)

    symbol = task.get_pair()
    order_id = task.get_buy_order_id()
    response = get_order_status(symbol, order_id)

    if response:
        if response['status'] == 'FILLED':

            actual_position_size = response['cummulativeQuoteQty']
            task.set_position_size(actual_position_size)

            actual_buy_price = str(d(actual_position_size) / d(response['executedQty']))
            task.set_buy_price(actual_buy_price)

            next_step = 'SELL'
            task.set_next_step(next_step)

    return task

def execute_sell(task : Task):
    print('execute_sell...')
    task = deepcopy(task)

    # calculate take profit and stop loss price
    symbol = task.get_pair()
    step_size = get_step_size(symbol)
    tick_size = get_tick_size(symbol)
    risk = task.get_risk()
    reward = task.get_reward()
    entry_price = task.get_buy_price()
    position_size = task.get_position_size()
    coin =  symbol.replace(base_coin, '')

    price = get_take_profit(reward, position_size, entry_price)
    stopPrice = get_stop_loss(risk, position_size, entry_price)
    stopLimitPrice = get_product(stopPrice, '0.90')
    quantity = get_balance(coin)

    # create oco order
    response = oco_sell_order(
        symbol = symbol,
        quantity = roundoff_num(quantity, tick_size),
        price = roundoff_num(price, step_size),
        stopPrice = roundoff_num(stopPrice, step_size),
        stopLimitPrice = roundoff_num(stopLimitPrice, step_size)
    )

    # save order id's
    if response:
        for order in response['orderReports']:
            orderId = order['orderId']
            if order['type'] == 'LIMIT_MAKER':
                task.set_take_profit_order_id(orderId)
            if order['type'] == 'STOP_LOSS_LIMIT':
                task.set_stop_loss_order_id(orderId)

    return task

def execute_wait_sell(task : Task):
    print('execute_wait_sell...')
    task = deepcopy(task)
    return task

def execute_done(task : Task):
    print('execute_done...')
    task = deepcopy(task)
    return task

def execute_cancel(task : Task):
    print('execute_cancel...')
    task = deepcopy(task)
    return task
