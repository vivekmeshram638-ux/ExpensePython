import streamlit as st
import pandas as pd

st.title("📊 Expense Dashboard")

file = "expenses.csv"


# Safely load expenses: create the file with headers if missing/empty
def load_expenses(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
        df.to_csv(path, index=False)
        return df


# Load the data and handle the empty case gracefully
df = load_expenses(file)

if df.empty:
    st.info("No expenses recorded yet. Add one from the sidebar.")
else:
    st.write("Category Wise Expense")

    category_data = df.groupby("Category")["Amount"].sum()

    st.bar_chart(category_data)

    st.write("Expense Distribution")
    st.write(category_data)

    st.write("Monthly Expense")

    df["Date"] = pd.to_datetime(df["Date"])

    monthly = df.groupby(df["Date"].dt.month)["Amount"].sum()

    st.line_chart(monthly)