import streamlit as st
import pandas as pd

st.title("👀 View Expenses")

file = "expenses.csv"

# Safely load expenses; create the file with headers if missing/empty

def load_expenses(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
        df.to_csv(path, index=False)
        return df


# Load data and handle the empty-case gracefully
df = load_expenses(file)

if df.empty:
    st.info("No expenses recorded yet. Add one from the sidebar.")
else:
    st.dataframe(df)

    st.write("Total Expense")
    total = df["Amount"].sum()
    st.success(f"Total: ${total:.2f}")

    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="expenses.csv",
        mime="text/csv"
    )