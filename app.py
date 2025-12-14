import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sales & Profit Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA & MODEL ----------------
df = pd.read_csv("data/cleaned_sales_data.csv")
model = joblib.load("model/profit_model.pkl")

st.title("📊 Sales, Profit & Pricing Analytics Dashboard")

# ---------------- MODE TOGGLE ----------------
mode = st.radio(
    "Prediction Mode",
    ["Pure ML", "Business-Adjusted"],
    horizontal=True,
    help="Pure ML uses the trained model only. Business-Adjusted enforces financial logic."
)

# ================= KPI SECTION =================
st.subheader("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{df['sales'].sum():,.0f}")
col2.metric("Total Profit", f"{df['profit'].sum():,.0f}")
col3.metric("Units Sold", f"{df['units_sold'].sum():,.0f}")
col4.metric(
    "Avg Margin (%)",
    f"{(df['profit'].sum() / df['sales'].sum()) * 100:.2f}"
)

# ================= TIME TREND =================
st.subheader("Sales & Profit Over Time")

yearly = df.groupby("year")[["sales", "profit"]].sum()

fig, ax = plt.subplots()
ax.plot(yearly.index, yearly["sales"], marker="o", label="Sales")
ax.plot(yearly.index, yearly["profit"], marker="o", label="Profit")
ax.set_xlabel("Year")
ax.set_ylabel("Amount")
ax.legend()
st.pyplot(fig)

# ================= COUNTRY PERFORMANCE =================
st.subheader("Top Countries by Sales")

top_countries = (
    df.groupby("country")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
top_countries.plot(kind="bar", ax=ax)
ax.set_ylabel("Sales")
st.pyplot(fig)

# ================= PROFIT SIMULATOR =================
st.subheader("💡 Profit Simulator")

units = st.slider("Units Sold", 0, 5000, 1000)
sale_price = st.slider("Sale Price (per unit)", 1.0, 100.0, 20.0)
manufacturing_price = st.slider("Manufacturing Cost (per unit)", 1.0, 100.0, 12.0)
discount = st.slider("Total Discount Amount", 0.0, 10000.0, 500.0)
month = st.selectbox("Month", list(range(1, 13)))

# ---------------- FEATURE ENGINEERING (MATCHES COLAB) ----------------
unit_margin = sale_price - manufacturing_price
gross_revenue = sale_price * units

discount_ratio = (
    discount / gross_revenue if gross_revenue > 0 else 0
)

input_df = pd.DataFrame([{
    "units_sold": units,
    "unit_margin": unit_margin,
    "discount_ratio": discount_ratio,
    "month": month
}])

# ---------------- PREDICTIONS ----------------
ml_profit = model.predict(input_df)[0]

# Rule-based (business logic) profit
rule_profit = (sale_price - manufacturing_price) * units - discount

# Final output based on toggle
if mode == "Pure ML":
    final_profit = ml_profit
else:
    final_profit = rule_profit

# ---------------- DISPLAY RESULT ----------------
st.success(f"Predicted Profit: ₹{final_profit:,.2f}")

# ---------------- EXPLANATION ----------------
with st.expander("ℹ️ How this prediction is computed"):
    st.write(
        """
        **Pure ML**: Uses a machine learning model trained on historical data with 
        business-aware features (unit margin, discount ratio, seasonality).

        **Business-Adjusted**: Applies direct financial logic:
        Profit = (Sale Price − Manufacturing Cost) × Units Sold − Discounts.

        This hybrid approach ensures predictions respect real-world financial constraints.
        """
    )