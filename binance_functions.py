from binance.client import Client
from binance.enums import *
from config import api_key, api_secret

client = Client(api_key, api_secret)

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

def get_balance(asset):
    return client.get_asset_balance(asset=asset)['free']

def hello():
    print("hello")


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