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