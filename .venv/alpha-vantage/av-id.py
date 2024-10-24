from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os
import pandas as pd

def configure():
    load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

ts = TimeSeries(key='ALPHAVANTAGE_API_KEY')

#Invokethe intraday() method. You must pass the ticker value (IBM) to the intraday() method.

data, metadata = ts.get_intraday(symbol='IBM')
print(metadata)

df = pd.DataFrame(data)
df.head().T #a tuple containing the response’s data and metadata. 
# Converting the response into a Pandas dataframe
