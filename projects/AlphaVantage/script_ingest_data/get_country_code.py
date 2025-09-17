import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def get_data():
    response = requests.get("https://www.iban.com/country-codes")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        df = pd.read_html(str(soup))
        df1 = pd.DataFrame(df[0], index=None)
        df1.to_csv('/home/anhtt1/Workspace/DE/Project/DE_Project/projects/AlphaVantage/data/country_codes.csv', index=False)
        logging.info("Country codes saved to '/home/anhtt1/Workspace/DE/Project/DE_Project/projects/AlphaVantage/data/country_codes.csv'")
    else:
        logging.error(f"Failed to retrieve data: {response.status_code}")

def main():
    get_data()

if __name__ == "__main__":
    main()