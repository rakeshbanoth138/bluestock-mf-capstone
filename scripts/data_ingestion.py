from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

csv_files = sorted(raw_path.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files")

for file in csv_files:
    print("\n" + "="*60)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())