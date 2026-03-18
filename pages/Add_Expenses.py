import streamlit as st
import pandas as pd
from datetime import date

# Page title in Streamlit
st.title("➕ Add Expense")

# CSV file used to store expenses
file = "expenses.csv"

# Safely load expenses; create the file with headers if missing/empty
def load_expenses(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
        df.to_csv(path, index=False)
        return df

# Ensure the file exists with the expected headers
load_expenses(file)

# --- Form inputs ---
# Date picker defaults to today's date
expense_date = st.date_input("Date", date.today())

# Category selection dropdown
category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Other"]
)

# Numeric input for the expense amount
amount = st.number_input("Amount :", min_value=0.0)

# Optional note/description for the expense
note = st.text_input("Note")

# When the user clicks the button, append the new expense to the CSV
if st.button("Add Expense"):
    # Load existing expenses
    df = load_expenses(file)
    # Create a one-row DataFrame for the new expense
    new_data = pd.DataFrame({
        "Date": [expense_date],
        "Category": [category],
        "Amount": [amount],
        "Note": [note]
    })
    
    # Append the new entry and save back to disk
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file, index=False)
    
    st.success("Expense added Successfully")