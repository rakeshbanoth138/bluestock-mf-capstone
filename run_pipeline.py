

import subprocess

scripts = ["scripts/data_ingestion.py","scripts/data_cleaning.py","scripts/load_to_sqlite.py","scripts/recommender.py"]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])

print("Pipeline completed successfully.")