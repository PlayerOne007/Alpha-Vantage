from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os
import pandas as pd

def configure():
    load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

ts = TimeSeries(key='ALPHAVANTAGE_API_KEY')

data, metadata = ts.get_intraday(symbol='IBM')
print(metadata)

df = pd.DataFrame(data)
df.head().T
