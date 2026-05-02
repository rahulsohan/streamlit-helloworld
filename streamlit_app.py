import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.title("Hello World")

with st.sidebar:
    st.header("About App")
    st.header("My name is Joshua")
st.header("This is a header with a divider", divider="gray")

col1, col2 = st.columns(2)

with col1:
    x = st.slider("choose a value")
with col2:
    st.write("This is the selectedvalue", x)






st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
