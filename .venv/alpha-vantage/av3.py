import requests


import pandas as pd


API_key = '2J4OBFKDERRUM0TS'
url = 'https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=2J4OBFKDERRUM0TS'
r = requests.get(url)
data = r.json()


print(data["data"])
