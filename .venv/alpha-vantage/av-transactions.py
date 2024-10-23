import os

from urllib.request import urlopen
import json

API_key = 'FEVLG3U70K6KSKVY'

api_url =  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_key}'

with urlopen(url) as response:
    body = response.read()

data = json.loads(body)

print(data)