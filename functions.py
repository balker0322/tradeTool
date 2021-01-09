from decimal import Decimal as d
from model import Task
from copy import deepcopy
from binance_api import *
import time

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

def get_available_pairs(base_symbol : str):
    return get_all_pairs(base_symbol)

def execute_task(task : Task):
    task = deepcopy(task)
    next_step = task.get_next_step()
    current_step = next_step
    task_id = task.get_id()

    if current_step == 'BUY':
        '''
        response = buy_order(target_price, target_quantity)
        if response:
            # update step to checking buy order status
            pass
        
        '''
        print('ID{}: creating buy order..'.format(task_id))
        time.sleep(1)
        next_step = 'GET_BUY_ORDER_STATUS'

    if current_step == 'GET_BUY_ORDER_STATUS':
        '''
        response = check_buy_order_status()
        if response:
            if response['status'] == 'FILLED':
                actual_position_size = response['cummulativeQuoteQty']
                actual_price = str(d(actual_position_size) / d(response['executedQty']))
                # update step to create sell order
        '''
        print('ID{}: waitng buy order to finish..'.format(task_id))
        time.sleep(1)
        next_step = 'SELL'

    if current_step == 'SELL':
        '''
        # calculate take profit price
        # calculate stop loss price
        # submit oco order
        # if success response, proceed to next step
        '''
        print('ID{}: creating sell order..'.format(task_id))
        time.sleep(1)
        next_step = 'GET_BUY_SELL_STATUS'

    if current_step == 'GET_BUY_SELL_STATUS':
        '''
        # get sell order status
        # if sell order filled, calculate actual profit or loss
        '''
        print('ID{}: waitng buy order to finish..'.format(task_id))
        time.sleep(1)
        next_step = 'DONE'

    if current_step == 'DONE':
        # print('ID:{} task done'.format(task_id))
        task.set_task_to_inactive()

    if current_step == 'CANCEL':
        print('ID:{} cancel'.format(task_id))
        task.set_task_to_inactive()

    task.set_next_step(next_step)

    return task