from binance.client import Client
from binance.enums import *
from decimal import Decimal as d
from config import api_key, api_secret,BASE_COIN, MAX_PERCENT_QUANTITY
import pickle

base_coin = BASE_COIN
max_percent_quantity = MAX_PERCENT_QUANTITY

client = Client(api_key, api_secret)
test = True


test_order_status = {'symbol': 'BTCUSDT',
    'orderId': 3961371312,
    'orderListId': 11389820,
    'clientOrderId': 'Xa6oe6hgEFVJgHe7vA1pB6',
    'price': '23400.00000000',
    'origQty': '0.00100000',
    'executedQty': '0.00000000',
    'cummulativeQuoteQty': '0.00000000',
    'status': 'NEW',
    'timeInForce': 'GTC',
    'type': 'STOP_LOSS_LIMIT',
    'side': 'SELL',
    'stopPrice': '23450.00000000',
    'icebergQty': '0.00000000',
    'time': 1608444879688,
    'updateTime': 1608444879688,
    'isWorking': False,
    'origQuoteOrderQty': '0.00000000'}


def limit_buy_order(symbol, quantity, Price):
    print("limit_buy_order({symbol}, {quantity}, {Price})".format(symbol, quantity, Price))
    pass


def market_buy_order(symbol, quantity):
    try:
        buy_order = client.order_market_buy(
        symbol=symbol,
        quantity=quantity)
        return buy_order
    except:
        return False


def oco_sell_order(symbol, quantity, Price, stopPrice, stopLimitPrice):
    pass


def get_order_status(symbol, orderId):
    if test:
        return test_order_status

    return client.get_order(
        symbol=symbol,
        orderId=orderId)




def get_balance(asset=False):
    if asset:
        return client.get_asset_balance(asset=asset)
    return client.get_account()['balances']


def get_non_zero_balance():
    non_zero_balance = []
    for balance in get_balance():
        amount = balance['free']
        if float(amount) == 0.0:
            continue
        non_zero_balance.append(balance)
    return non_zero_balance


def get_equivalent(amount, original_sym, equavalent_sym):

    '''
    this function converts amount in certain symbol to equivalent
    amount on another symbol

    example:
    convert 1 BTC to USDT
    get_equivalent('1', 'BTC', 'USDT')
    '''

    if original_sym == equavalent_sym:
        return amount

    ticker = get_ticker(original_sym+equavalent_sym)
    if ticker:
        return str(d(amount)*d(ticker))

    ticker = get_ticker(equavalent_sym+original_sym)
    if ticker:
        return str(d(amount)/d(ticker))

    return False


def get_ticker(symbol):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)['price']
    except:
        ticker = False
    return ticker


def get_equity(base_symbol=base_coin):
    all_balances = get_non_zero_balance()
    total_equity = d('0.0')
    for balance in all_balances:
        amount = balance['free']
        original_sym = balance['asset']
        equivalent_amount = get_equivalent(amount = amount,
                                           original_sym = original_sym,
                                           equavalent_sym = base_symbol)
        if equivalent_amount:
            total_equity += d(equivalent_amount)
    return str(total_equity)


def get_raw_exchange_info():

    # check if file is available
    try:
        with open('binance_api/exchange_info', 'rb') as file:
            exchange_info = pickle.load(file)
    except:
        try:
            exchange_info = client.get_exchange_info()
            symbol_info = dict()
            for sym in exchange_info['symbols']:
                symbol = sym['symbol']
                symbol_info[symbol] = sym
            exchange_info['symbols'] = symbol_info
        except:
            return False

    # else create new file
    with open('binance_api/exchange_info', 'wb') as file:
        pickle.dump(exchange_info, file)

    return exchange_info


def get_all_pairs():
    exchange_info = get_raw_exchange_info()
    if exchange_info:
        pairs = []
        for info in exchange_info['symbols']:
            pairs.append(info['symbol'])
        return pairs
    return False


def get_symbol_info(pair):
    try:
        symbol_info = get_raw_exchange_info()['symbols'][pair]
        if symbol_info:
            return symbol_info
    except:
        pass
    return False


def get_tick_size(pair):
    info = get_symbol_info(pair)
    if info:
        return info['filters'][0]['tickSize']
    return False


def get_step_size(pair):
    info = get_symbol_info(pair)
    if info:
        return info['filters'][2]['stepSize']
    return False


def get_max_buy_quantity(pair, base_symbol = base_coin, max_percent_quantity = max_percent_quantity):
    balance = get_balance(base_symbol)['free']
    ticker = get_ticker(pair)
    max_quantity = d(balance) / d(ticker)
    max_quantity *= d(max_percent_quantity)
    step_size = d(get_step_size(pair))
    return str(float(max_quantity-max_quantity%step_size))


def get_max_sell_quantity():
    pass



def hello(name = None):
    if name:
        return name
    return "hi"


if __name__ == "__main__":
    print ("name is main")


'''
buy_order = client.order_market_buy(
    symbol='BTCUSDT',
    quantity=0.001)

oco_order = client.create_oco_order(
    symbol='BTCUSDT',
    side='SELL',
    quantity=0.00100000,
    price='23600',
    stopPrice='23450',
    stopLimitPrice='23400',
    stopLimitTimeInForce='GTC')

{'orderListId': 11389820,
 'contingencyType': 'OCO',
 'listStatusType': 'EXEC_STARTED',
 'listOrderStatus': 'EXECUTING',
 'listClientOrderId': '8CwRTW9k8GGT0h5fxsSoxg',
 'transactionTime': 1608444879688,
 'symbol': 'BTCUSDT',
 'orders': [{'symbol': 'BTCUSDT',
   'orderId': 3961371312,
   'clientOrderId': 'Xa6oe6hgEFVJgHe7vA1pB6'},
  {'symbol': 'BTCUSDT',
   'orderId': 3961371313,
   'clientOrderId': 'jbJadDew4cZgnxlXnCMKya'}],
 'orderReports': [{'symbol': 'BTCUSDT',
   'orderId': 3961371312,
   'orderListId': 11389820,
   'clientOrderId': 'Xa6oe6hgEFVJgHe7vA1pB6',
   'transactTime': 1608444879688,
   'price': '23400.00000000',
   'origQty': '0.00100000',
   'executedQty': '0.00000000',
   'cummulativeQuoteQty': '0.00000000',
   'status': 'NEW',
   'timeInForce': 'GTC',
   'type': 'STOP_LOSS_LIMIT',
   'side': 'SELL',
   'stopPrice': '23450.00000000'},
  {'symbol': 'BTCUSDT',
   'orderId': 3961371313,
   'orderListId': 11389820,
   'clientOrderId': 'jbJadDew4cZgnxlXnCMKya',
   'transactTime': 1608444879688,
   'price': '23600.00000000',
   'origQty': '0.00100000',
   'executedQty': '0.00000000',
   'cummulativeQuoteQty': '0.00000000',
   'status': 'NEW',
   'timeInForce': 'GTC',
   'type': 'LIMIT_MAKER',
   'side': 'SELL'}]}



order_stat = client.get_order(
    symbol='BTCUSDT',
    orderId=3961251473)

order_stat
{'symbol': 'BTCUSDT',
 'orderId': 3961371312,
 'orderListId': 11389820,
 'clientOrderId': 'Xa6oe6hgEFVJgHe7vA1pB6',
 'price': '23400.00000000',
 'origQty': '0.00100000',
 'executedQty': '0.00000000',
 'cummulativeQuoteQty': '0.00000000',
 'status': 'NEW',
 'timeInForce': 'GTC',
 'type': 'STOP_LOSS_LIMIT',
 'side': 'SELL',
 'stopPrice': '23450.00000000',
 'icebergQty': '0.00000000',
 'time': 1608444879688,
 'updateTime': 1608444879688,
 'isWorking': False,
 'origQuoteOrderQty': '0.00000000'}
'''