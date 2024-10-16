from alpha_vantage.timeseries import TimeSeries

API_key = '2J4OBFKDERRUM0TS'

ts = TimeSeries(key = API_key,output_format='pandas')

data = ts.get_monthly_adjusted('MSFT')

data[0]