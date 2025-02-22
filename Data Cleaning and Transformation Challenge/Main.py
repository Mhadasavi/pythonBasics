import gzip
import shutil
from pathlib import Path
import pandas as pd
from SilverSchema import SilverSchema
from SilverTransformation import AddScrapeDate


class AirBnb:
    def __init__(self, input_dir=r'Res\listings.gz', output_dir=r'Res\airbnb_listing.csv'):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)

    def read_and_decompress_data(self):
        """Decompresses a gzip file to a CSV file."""
        if not self.input_dir.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_dir}")

        with gzip.open(self.input_dir, 'rb') as f_in, open(self.output_dir, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    def load_to_pandas(self) -> pd.DataFrame:
        """Reads the decompressed CSV into a pandas DataFrame."""
        self.read_and_decompress_data()
        return pd.read_csv(self.output_dir)

    def get_silver_table(self) -> pd.DataFrame:
        """Filters DataFrame to include only the SilverSchema columns."""
        df = self.load_to_pandas()
        required_columns = [col for col in SilverSchema.SILVER_COLUMNS if col in df.columns]
        return df[required_columns].copy()

    def silver_pre_transforms(self):
        """Applies pre-transformations before further processing."""
        df = self.get_silver_table()
        AddScrapeDate.transform(df)
        return df  # Returning df in case further processing is needed

    # Inspect data

    # Data cleaning

    # Data transformation

    # Data validation and export

if __name__ == "__main__":
    airbnb = AirBnb()
    silver_df = airbnb.silver_pre_transforms()
    print(silver_df.head())  # Preview transformed DataFrame
