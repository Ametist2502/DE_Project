import requests
import pandas as pd
import os

API_KEY = os.getenv("COINGECKO_API_KEY", "")

def get_ohlc_data(coin_id, vs_currency="usd", days=1, precision="full"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc"
    querystring = {"vs_currency": vs_currency, "days": days, "precision": precision}
    headers = {"x-cg-demo-api-key": API_KEY} if API_KEY else {}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = pd.DataFrame(response.json(), columns=['timestamp', 'open', 'high', 'low', 'close'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
    
def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def incremental_update(existing_df, new_data):
    existing_df["timestamp"] = pd.to_datetime(existing_df["timestamp"])
    new_data["timestamp"] = pd.to_datetime(new_data["timestamp"])
    # Tìm những timestamp có ở new_data nhưng không có ở existing_df
    missing_timestamps = new_data.loc[~new_data["timestamp"].isin(existing_df["timestamp"])]
    
    # Thêm các dòng thiếu vào existing_df
    updated_df = pd.concat([existing_df, missing_timestamps], ignore_index=True)
    
    # Sắp xếp lại theo timestamp
    updated_df = updated_df.sort_values("timestamp").reset_index(drop=True)
    
    return updated_df