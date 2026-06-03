
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


SELECT AVG(nav) AS avg_nav
FROM fact_nav;


SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


SELECT amfi_code, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;


SELECT transaction_type,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;


SELECT SUM(amount_inr) AS total_investment
FROM fact_transactions;


SELECT state,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


SELECT risk_category,
       COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category;