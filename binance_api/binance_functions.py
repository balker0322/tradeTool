from binance.client import Client
from binance.enums import *
from decimal import Decimal as d
from config import api_key, api_secret,BASE_COIN, MAX_PERCENT_QUANTITY
import pickle
from .sample_response import *

base_coin = BASE_COIN
max_percent_quantity = MAX_PERCENT_QUANTITY

client = Client(api_key, api_secret)
test = True

def limit_buy_order(symbol, quantity, Price):
    print("limit_buy_order({symbol}, {quantity}, {Price})".format(symbol, quantity, Price))
    pass


def market_buy_order(symbol, quantity):
    if test:
        return test_market_buy_order

    try:
        response = client.order_market_buy(
        symbol=symbol,
        quantity=quantity)
        return response
    except:
        return False

def oco_sell_order(symbol, quantity, price, stopPrice, stopLimitPrice, stopLimitTimeInForce = 'GTC'):
    if test:
        return test_oco_sell_order

    try:
        response = client.create_oco_order(
                    symbol = symbol,
                    side = 'SELL',
                    quantity = quantity,
                    price = price,
                    stopPrice = stopPrice,
                    stopLimitPrice = stopLimitPrice,
                    stopLimitTimeInForce = stopLimitTimeInForce)
        return response
    except:
        return False


def get_order_status(symbol, orderId):
    if test:
        return test_order_status
    try:
        order_status = client.get_order(
        symbol=symbol,
        orderId=orderId)
        return order_status
    except:
        return False




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
    step_size = get_step_size(pair)
    return roundoff_num(str(max_quantity), step_size)


def roundoff_num(number, min_step):
    res = d(number)-(d(number)%d(min_step))
    res = str(res)
    res = res.rstrip('0').rstrip('.') if '.' in res else res
    return res


def get_max_sell_quantity():
    pass



def hello(name = None):
    if name:
        return name
    return "hi"


if __name__ == "__main__":
    print ("name is main")

