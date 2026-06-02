import requests
import pandas as pd
from pathlib import Path

scheme_codes = [
    125497,  # HDFC Top 100
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

save_path = Path("data/raw")

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            filename = save_path / f"nav_{code}.csv"

            nav_df.to_csv(filename, index=False)

            print(f"Downloaded: {filename}")

        else:
            print(f"Failed for {code}")

    except Exception as e:
        print(f"Error for {code}: {e}")