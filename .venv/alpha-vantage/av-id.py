from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd

api_key = 'FEVLG3U70K6KSKVY'

ts = TimeSeries(key=api_key)

data, metadata = ts.get_intraday(symbol='IBM')
print(metadata)

df = pd.DataFrame(data)
df.head().T