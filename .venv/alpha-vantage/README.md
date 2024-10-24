# Alpha Vantage 

## Restful backend service

GET/transactions (Returns parginated list of all transactions)

```
import os

from urllib.request import urlopen
import json

API_key = 'FEVLG3U70K6KSKVY'

api_url =  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_key}'

with urlopen(url) as response:
    body = response.read()

data = json.loads(body)

print(data)

```
GET /transactions/{id}

```
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd

api_key = 'FEVLG3U70K6KSKVY'

ts = TimeSeries(key=api_key)

data, metadata = ts.get_intraday(symbol='IBM')
print(metadata)

df = pd.DataFrame(data)
df.head().T
```
GET /transactions/time-series?start={startDate}&end={endDate}

```
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

api_key = '2J4OBFKDERRUM0TS'

ts = TimeSeries(key=api_key, output_format='CSV')

data_csv,_ = ts.get_intraday("IBM")

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