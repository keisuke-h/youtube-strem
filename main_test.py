import streamlit as st
import time

st.title('streamlit　超入門')

st.write('ブログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('お問合せ')
expander.write('問合せ内容を各')


text = st.text_input('あなたの趣味をおしえてください')
condition = st.slider('あなたの今の調子は', 0, 100, 50)

'あなたが好きな趣味は', text, 'です'
'コンディション', condition
