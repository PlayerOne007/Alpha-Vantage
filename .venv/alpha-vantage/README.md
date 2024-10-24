# Alpha Vantage 

## Restful backend service

GET/transactions (Returns parginated list of all transactions)

```
from dotenv import load_dotenv
import os

from urllib.request import urlopen
import json

def configure():
    load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

api_url =  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={'ALPHAVANTAGE_API_KEY'}'

with urlopen(url) as response:
    body = response.read()

data = json.loads(body)

print(data)
```
GET /transactions/{id}

```
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
```
GET /transactions/time-series?start={startDate}&end={endDate}

```
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
```
Note: To run the code, you can run the following command:
```
python3 <filename.py>
```
or 

Right click and run Python file on the Terminal