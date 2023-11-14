import streamlit as st
import numpy as np
import pandas as pd
import time
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

#st.write('Display Image')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander=st.expander('問合せ')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')

#st.write('Interactive Widgets')
#text = st.text_input('あなたの趣味を教えて下さい。')
#'あなたの趣味: ', text, 'です。'
#condition=st.slider('あなたの今の調子は？', 0, 100, 50)
#'コンディション:', condition, 'です。' 

#option=st.selectbox(
#    'あなたが好きな数字教えて下さい。', 
#    list(range(1,11))
#)
#
#'あなたの好きな数字は、', option, 'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('RA21-X9M-eth1-2-9-10-cardcheck.jpg')
#    st.image(img, caption='RA21 EtherCard',use_column_width=True)









