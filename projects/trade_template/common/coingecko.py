import requests
import pandas as pd

def get_ohlc_data(coin_id, vs_currency="usd", days=1, precision="full"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc"
    querystring = {"vs_currency": vs_currency, "days": days, "precision": precision}
    headers = {"x-cg-demo-api-key": ""}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = pd.DataFrame(response.json(), columns=['timestamp', 'open', 'high', 'low', 'close'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        return data
    else:
        print(f"Error: {response.status_code}")
        return None