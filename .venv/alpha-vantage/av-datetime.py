# Fetching Data Using Alpha Vantage API 
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


from alpha_vantage.timeseries import TimeSeries
import pandas as pd

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

# From the alpha_vantage to get time series intraday trading data.timeseries module

ts = TimeSeries(key='ALPHAVANTAGE_API_KEY', output_format='CSV')

data_csv,_ = ts.get_intraday("IBM") # Invoke the intraday() method

for index, row in enumerate(data_csv):
    print(', '.join(row))
    if index > 5:
        break
# response in CSV format by passing `CSV` as the value for the `output_format` attribute of the TimeSeries class.