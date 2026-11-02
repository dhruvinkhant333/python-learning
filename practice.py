import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Sample dataset
df = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Category": ["Laptop", "Mobile", "Laptop", "Mobile", "Tablet", "Laptop"],
        "Sales": [120, 180, 150, 220, 130, 260],
        "Profit": [20, 35, 25, 45, 22, 55],
    }
)

st.title("Interconnected Sales Dashboard")

# Interactive filter
categories = st.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=list(df["Category"].unique()),
)
filtered = df[df["Category"].isin(categories)]

# KPI cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", int(filtered["Sales"].sum()))
with col2:
    st.metric("Total Profit", int(filtered["Profit"].sum()))
with col3:
    average_sales = round(filtered["Sales"].mean(), 2) if not filtered.empty else 0.0
    st.metric("Average Sales", average_sales)

# Connected charts
left, right = st.columns(2)
with left:
    fig1 = px.bar(filtered, x="Month", y="Sales", color="Category", title="Monthly Sales")
    st.plotly_chart(fig1, width="stretch")
with right:
    fig2 = px.line(
        filtered,
        x="Month",
        y="Profit",
        color="Category",
        markers=True,
        title="Monthly Profit",
    )
    st.plotly_chart(fig2, width="stretch")

st.subheader("Filtered Data")
st.dataframe(filtered, width="stretch")

# Install:
# pip install streamlit pandas plotly
# Run:
# streamlit run practice.py
