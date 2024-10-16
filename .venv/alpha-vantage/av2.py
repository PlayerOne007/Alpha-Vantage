import requests


import pandas as pd


API_key = '2J4OBFKDERRUM0TS'


url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=2J4OBFKDERRUM0TS'


r = requests.get(url)


data = r.json()


print(data["Time Series FX (Daily)"])

pd.DataFrame(data["Time Series FX (Daily)"]).transpose()