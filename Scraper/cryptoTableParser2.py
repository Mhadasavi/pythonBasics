import requests
import pandas as pd
from bs4 import BeautifulSoup

class CryptoTableParser2:

    def get_crypto_data(self):
        url = 'https://crypto.com/price'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'chakra-table css-1qpk7f7'}) #chakra-table css-1qpk7f7
        data = []
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            name_tag = columns[2].find('p', class_='chakra-text css-rkws3')
            name = name_tag.get_text(strip=True) if name_tag else 'N/A'
            data.append({'Name': name})
            # price = columns[3].find('p', class_='chakra-text css-13hqrwd').get_text(strip=True)
            # change_24h = columns[4].get_text(strip=True)
            # data.append({'Name': name, 'Price': price, '24H Change': change_24h})
        print(pd.DataFrame(data))
        return data
        # for entry in data:
        #     print(f"Name: {entry['Name']}, Price: {entry['Price']}, 24H Change: {entry['24H Change']}")

        # store in pandas df
        # print(pd.DataFrame(data))
        # return data
    # store in pyspark df

    # export in excel using pyspark.write
