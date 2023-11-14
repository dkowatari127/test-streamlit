import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

st.bar_chart(df)
#st.table(df.style.highlight_max(axis=0))

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df2)

st.write('Display Image')
img = Image.open('RA21-X9M-eth1-2-9-10-cardcheck.jpg')
st.image(img, caption='RA21 EtherCard')







