from alpha_vantage.timeseries import TimeSeries
import pandas as pd

api_key = '2J4OBFKDERRUM0TS'

ts = TimeSeries(key=api_key, output_format='CSV')

data_csv,_ = ts.get_intraday("IBM")

for index, row in enumerate(data_csv):
    print(', '.join(row))
    if index > 5:
        break