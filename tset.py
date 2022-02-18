import datetime
import time
import pyupbit

df = pyupbit.get_ohlcv('KRW-BTC', interval="minute3", count=1)
print(df['high'])