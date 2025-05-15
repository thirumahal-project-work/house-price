

import streamlit as st
import pandas as pd

st.title("Housing Data Explorer")

# Upload CSV file or use default
uploaded_file = st.file_uploader("Upload Housing.csv", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("Housing.csv")  # assumes it's in the same directory

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Dataset Info")
buffer = []
df.info(buf=buffer)
st.text("\n".join(buffer))

st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Missing Values")
st.write(df.isnull().sum())

