import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit　超入門')

st.write('DateFrame')

df = pd.DateFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[1, 2, 3, 4]
})

st.dateFrame(df)