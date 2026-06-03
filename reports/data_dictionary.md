


| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Asset Management Company |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct/Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Annual expense ratio |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP amount |
| min_lumpsum_amount | REAL | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk classification |
| sebi_category_code | TEXT | SEBI category code |

---



| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---


| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| alpha | REAL | Alpha measure |
| beta | REAL | Beta measure |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk-adjusted return |
| expense_ratio_pct | REAL | Fund expense ratio |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |