import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")

z_data = pd.read_csv(‘https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv 26’)
z = z_data.values

st.write(1234)
st.write(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],}))
