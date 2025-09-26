from common.coingecko import get_ohlc_data, compute_rsi, incremental_update
import pandas as pd

def main():
    # Đường dẫn tới file dữ liệu cũ

    old_data_path = '/home/anhtt1/Workspace/DE/Project/DE_Project/projects/trade_template/data/bitcoin_ohlc_with_indicators.csv'
    df = pd.read_csv(old_data_path)
    incremental_data = get_ohlc_data(coin_id='bitcoin', vs_currency='usd', days=1, precision='full')
    incremental_data["EMA_20"] = incremental_data["close"].ewm(span=20, adjust=False).mean()
    incremental_data["EMA_50"] = incremental_data["close"].ewm(span=50, adjust=False).mean()
    incremental_data["RSI_14"] = compute_rsi(incremental_data["close"], 14)

    df_updated = incremental_update(df, incremental_data)
    df_updated.to_csv(old_data_path, index=False)

if __name__ == "__main__":
    main()