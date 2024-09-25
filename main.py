import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose CSV file :", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by :", columns)
    unique_val = df[selected_column].unique()
    selected_val = st.selectbox("Select value :", unique_val)

    # plotting the values
    filtered_df = df[df[selected_column] == selected_val]
    st.write(filtered_df)

    st.subheader("Plot data :")
    x_column = st.selectbox("select your X-axis column.",columns)
    y_column = st.selectbox("select your y-axis column.",columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")