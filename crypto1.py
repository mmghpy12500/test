import requests
import sys

response = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{sys.argv[1]}/').json()
print(response[0]['price_usd'])