import streamlit as st
import numpy as np
import pandas as pd
import sqlite3 as sq
from sqlite3 import Connection
import time
from streamlit import caching
from streamlit import config

df = pd.read_csv('drivers.csv')
df.head()
sl= st.slider('Row Index', 0, df.index[-1], 30)
st.title('F1 Drivers')
if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(df.iloc[sl:sl+1])

tempComment = st.text_input(label="Comment:")

with open("comments.txt", 'wa') as f:
    f.writelines(tempComment)

if st.checkbox("Persistent", value=False):
    config.set_option("client.caching", True)
else:
    config.set_option("client.caching", False)


@st.cache(suppress_st_warning=True, persist=True)
def test_cache():
	time.sleep(2)
	st.text_area("Test from inside the file")

if st.button("Inside"):
	test_cache()

if st.button("Clear Cache"):
	caching.clear_cache()