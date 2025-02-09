import gzip
import shutil

import pandas as pd


class AirBnb:
    input_dir = "Res\listings.gz"
    output_dir = r'Res\airbnb_listing.csv'

    # Decompress csv data
    def read_and_decompress_data(self, input_path, output_file):
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    # Load into pandas
    def load_to_pandas(self, data):
        return pd.read_csv(data)

    # Inspect data

    # Data cleaning

    # Data transformation

    # Data validation and export

obj = AirBnb()
obj.read_and_decompress_data(obj.input_dir, obj.output_dir)
print(obj.load_to_pandas(obj.output_dir).columns)
