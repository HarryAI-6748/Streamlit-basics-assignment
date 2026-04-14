import streamlit as st
import pandas as pd

print("Create a Python file called sales_app.py that does the following" \
"Displays a title and a short subheader describing the app" \
" Creates a small hardcoded pandas DataFrame with at least 5 rows and 3 columns: Product, Category, and Sales " \
"Adds a selectbox that lets the user filter the table by Category" \
" Displays the filtered DataFrame using st.dataframe()")

st.title("Sales Data")
st.subheader("Month - Apr 26")

data = {
    "Product": ['Soap', 'T-shirt', 'Spoon', 'Brush', 'Trackpants'],
    "Category": ['Personal Use','Clothes','Utensils','Personal Use','Clothes'],
    "Sales": [2500, 7000, 500, 900, 5000]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.sidebar.title("Filters")

filter = st.sidebar.multiselect(
    "Select Category",
    options=['Personal Use','Clothes','Utensils'],
    default=['Utensils']
)

filtered_df = df[df["Category"].isin(filter)]
st.dataframe(filtered_df)