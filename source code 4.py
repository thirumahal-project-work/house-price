

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Distribution of 'price'
if 'price' in df.columns:
    st.subheader("Distribution of House Prices")
    fig, ax = plt.subplots()
    sns.histplot(df['price'], kde=True, ax=ax)
    ax.set_title("Distribution of House Prices")
    st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

# Boxplots for numerical columns
st.subheader("Boxplots for Numerical Columns")
numeric_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking']
for column in numeric_columns:
    if column in df.columns:
        fig, ax = plt.subplots()
        sns.boxplot(y=df[column], ax=ax)
        ax.set_title(f"Boxplot of {column}")
        st.pyplot(fig)