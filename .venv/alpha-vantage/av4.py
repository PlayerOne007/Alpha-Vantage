from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt




API_key = '2J4OBFKDERRUM0TS'


stock = "AAPL"


url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=2J4OBFKDERRUM0TS"


r = requests.get(url)


data = r.json()


datetime = r.json()


print(data, datetime)
