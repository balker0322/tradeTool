from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("BINANCE_API_KEY")
api_secret = os.environ.get("BINANCE_API_SECRET")

POSITION_SIZE_MIN = "0.10" # in percentage of equity
POSITION_SIZE_MAX = "1.00"
RR_RATIO_MIN = "0.30"
RR_RATIO_MAX = "2.00"
RISK_MIN = "0.001"
RISK_MAX = "0.020"
ENTRY_PRICE = "19000"
ADJUSTMENT_CONSTANT = "1.002" # for trading fees adjustment in calculation
TICK_SIZE = "0.01000000" # minimum price movement
LOT_SIZE = "0.00000100"
PAIR = "BTCUSDT"

BASE_COIN = 'USDT'
MAX_PERCENT_QUANTITY = '0.95' # maximum percentage of buy quantity