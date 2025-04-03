import streamlit as st
import pandas as pd

st.title("My Streamlit App")

if st.button("Click me!"):
    data= pd.read_csv("data.csv")
    st.write(data)