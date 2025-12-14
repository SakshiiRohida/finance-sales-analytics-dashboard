Finance Sales Analytics Dashboard

Business-Aware Profit Prediction and Analytics

Project Overview

This project is an end-to-end analytics system for analyzing sales, pricing, discounts, and profit using machine learning and business logic. It demonstrates why pure machine learning models can fail in finance-related problems and how business-aware modeling fixes those issues.

The system includes data cleaning, exploratory analysis, profit modeling, and an interactive Streamlit dashboard with a profit simulator.

The Core Problem

A profit prediction model trained purely on historical data can learn misleading correlations, such as:

Higher discounts appearing to increase profit

Manufacturing cost having little or no impact on profit

These patterns may be statistically valid but are financially incorrect.

Two Modeling Approaches Used
1. Pure Machine Learning Model

The Pure ML model predicts profit using historical patterns only.

Learns correlations from past data

Captures demand behavior and seasonality

Can violate financial logic when data is biased

This model is useful for understanding historical trends but is unreliable for decision-making without constraints.

2. Business-Aware Model (Improved Approach)

The Business-Aware model incorporates financial logic through feature engineering.

Key ideas:

Unit Margin = Sale Price − Manufacturing Cost

Discount Ratio = Discounts / Gross Revenue

This ensures:

Profit decreases when costs increase

Profit decreases when discounts increase

Machine learning is still used to model uncertain relationships, but non-negotiable business rules are enforced.

Dashboard Features

Sales and profit KPIs

Trend analysis over time

Country-level performance

Profit simulator with user-controlled inputs

Toggle to compare Pure ML predictions vs Business-Adjusted results

This allows users to clearly see how business logic changes model behavior.
