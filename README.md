Finance Sales Analytics Dashboard

An end-to-end sales and profit analytics system demonstrating why pure machine learning models fail in finance and how business-aware modeling fixes those failures.

Why this project exists

In real business settings, profit prediction models often learn misleading correlations from historical data.

Examples:

Discounts appear to increase profit

Manufacturing cost has little effect on profit

These patterns may be statistically valid but are financially incorrect.

This project addresses that gap.

Two modeling approaches
1. Pure Machine Learning Model

Trained only on historical data

Learns correlations and seasonal patterns

Can violate basic financial logic when data is biased

Useful for trend analysis, but unsafe for decision-making on its own.

2. Business-Aware Model (Improved)

Encodes non-negotiable financial logic using feature engineering

Uses:

Unit Margin = Sale Price − Manufacturing Cost

Discount Ratio = Discounts / Gross Revenue

Ensures:

Higher costs reduce profit

Higher discounts reduce profit

Machine learning is still used, but within business constraints.

What the dashboard shows

Sales and profit KPIs

Time-based trends

Country-level performance

Interactive profit simulator

Toggle to compare:

Pure ML predictions

Business-adjusted results

This makes model behavior transparent and interpretable.

Tech stack

Python

Pandas, NumPy

Scikit-learn (Random Forest)

Streamlit

Plotly / Matplotlib
