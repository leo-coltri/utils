import pandas as pd

def format_to_parquet(data_dir):
    for path, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(path, file)
                file_path_parquet = file_path.replace('.csv', '.parquet')
                df = pd.read_csv(file_path, sep=';', encoding='utf8', engine='python')
                df.to_parquet(file_path_parquet, compression='snappy')
