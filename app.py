import streamlit as st
import pandas as pd

st.title("My Streamlit App")

if st.button("Click me!"):
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)

        st.write(data)