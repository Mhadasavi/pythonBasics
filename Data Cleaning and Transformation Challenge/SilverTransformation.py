import pandas as pd
from datetime import datetime


class AddScrapeDate:
    @staticmethod
    def transform(df: pd.DataFrame):
        """Adds a `scrape_date` column to the DataFrame."""
        df["scrape_date"] = datetime.today().strftime('%Y-%m-%d')
