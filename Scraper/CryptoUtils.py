from bs4 import BeautifulSoup
from pyspark.sql import functions as F
import requests


def get_usd_to_inr():
    url = 'https://www.x-rates.com/calculator/?from=USD&to=INR&amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    exchange_rate = soup.find('span', {'class': 'ccOutputRslt'}).get_text(strip=True)
    trimmed_exchange_rate = exchange_rate[:5]
    return float(trimmed_exchange_rate)