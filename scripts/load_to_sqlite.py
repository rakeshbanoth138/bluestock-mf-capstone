import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/db/bluestock_mf.db")
conn = engine.connect()
print("Database created successfully")

# Load fund master dataset
fund_df = pd.read_csv("data/raw/01_fund_master.csv")
print("Fund Master Shape:", fund_df.shape)

fund_df.to_sql("dim_fund",engine,if_exists="replace",index=False)
print("dim_fund loaded successfully")

nav_df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
print("NAV Shape:", nav_df.shape)

nav_df.to_sql("fact_nav",engine,if_exists="replace",index=False)
print("fact_nav loaded successfully")

performance_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
print("Performance Shape:", performance_df.shape)
performance_df.to_sql("fact_performance",engine,if_exists="replace",index=False)
print("fact_performance loaded successfully")

transactions_df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

print("Transactions Shape:", transactions_df.shape)

transactions_df.to_sql("fact_transactions",engine,if_exists="replace",index=False)
print("fact_transactions loaded successfully")



result = conn.execute(text("SELECT COUNT(*) FROM dim_fund"))
print("Rows in dim_fund:", result.fetchone()[0])

result = conn.execute(text("SELECT COUNT(*) FROM fact_nav"))
print("Rows in fact_nav:", result.fetchone()[0])

result = conn.execute(text("SELECT COUNT(*) FROM fact_performance"))
print("Rows in fact_performance:", result.fetchone()[0])

result = conn.execute(text("SELECT COUNT(*) FROM fact_transactions"))
print("Rows in fact_transactions:", result.fetchone()[0])


conn.close()

print("All tables loaded successfully!")