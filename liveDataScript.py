import pandas as pd
import sqlalchemy
from binance.client import client
from binance import BinanceSocketManager

client = Client(api_key, api_secretKey)
bsm = BinanceSocketManager
socket = bsm.trade_socket('BTCUSDT')

while True:
await socket.__aenter__()
msg = await socket.recv()
frame = createframe(msg)

print(msg)

def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns = ['symbol','Time','Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df

createframe(msg)

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')