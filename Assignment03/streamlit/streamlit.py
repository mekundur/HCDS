#!/usr/bin/python3

import streamlit as st
import pandas as pd

@st.cache_data
def load_data_set(path):
    df = pd.read_csv(path)
    return df

df = load_data_set('german_credit_data_processed.csv')
# df.columns = df.columns.str.strip()
# print(df.head())
# print(df.nunique())

st.success("Data is succesfully loaded!")
st.subheader("German Credit Data", divider=True)
# st.title('German Credit Data')
st.dataframe(df.head(3))
# st.write(df.head())

st.subheader("Filter the Data by columns", divider=True)
filter1 = st.multiselect('Columns to display:', options=df.columns.tolist(), default=df.columns.tolist())
if not filter1:
    st.warning("Please select at least one coloumn!")
else:
    st.dataframe(df[filter1])

st.subheader("Filter the Data to show values Bar Charts", divider=True)
filter2 = st.selectbox("Columns to show", options = df.columns.tolist())
if not filter2:
    st.warning("Please select at least one coloumn!")
else:
    st.dataframe(df[filter2])
if df[filter2].nunique() < 20 or df[filter2].dtype == 'object':
    st.bar_chart(df[filter2].value_counts())
else:
    st.warning("Unable to build bar chart")


st.subheader("Filter the Data to show linear chart", divider=True)
numeric = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
filter3 = st.multiselect('Numeric columns to show', options = numeric)
if filter3:
    st.line_chart(df[filter3])
else:
    st.warning("Please select a data label")

st.subheader('Correlation Matrix')
correlation = df[numeric].corr()
st.dataframe(correlation)
