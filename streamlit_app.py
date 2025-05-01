import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("merged_output/final_merged_dataset.csv")

st.title("Chicago Housing Dashboard")

selected_zip = st.selectbox("Choose ZIP Code", sorted(df["ZipCode"].unique()))
filtered_df = df[df["ZipCode"] == selected_zip]

st.subheader("Housing Price")
st.write(f"Average Housing Price (2023): ${filtered_df['average_housing_cost_2023'].values[0]:,.0f}")

st.subheader("School Quality")
st.write(f"School Rating: {filtered_df['Overall_Rating'].values[0]}")

st.subheader("Crime")
st.write(f"Total Crimes: {filtered_df['Total_Crimes'].values[0]}")