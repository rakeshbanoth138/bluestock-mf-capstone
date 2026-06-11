"""Mutual Fund Recommendation Engine
Generates fund recommendations based on performance and risk metrics."""


import pandas as pd

funds = pd.read_csv("data/processed/01_fund_master_cleaned.csv")
sharpe = pd.read_csv("reports/sharpe_ratio.csv")

df = funds.merge(sharpe, on="amfi_code")

risk = input("Enter Risk Level (Low/Moderate/High): ")

result = (df[df["risk_category"].str.lower().str.contains(risk.lower())].sort_values("sharpe_ratio", ascending=False).head(3))

print(result[["scheme_name", "risk_category", "sharpe_ratio"]])