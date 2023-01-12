import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('インタラクティブなウィジェット')

#プログレスバー
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itaration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'




# #チェックボックス (ブーリアン型)
# if st.checkbox('Show Image'): 
#     img = Image.open('510-1.jpg')
#     st.image(img, caption='ペンギン', use_column_width=True)

# #セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,10))
# )

# 'あなたの好きな数字は、', option, 'です。'

# #テキストボックス
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text

# #スライダー
# condition = st.slider('あなたの今の調子は?', 0, 100, 50)
# 'コンディション；', condition



#レイアウト

# #サイドバー
# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション；', condition


# #カラム
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button: #ボタンが押されたら
#     right_column.write('ここは右カラム')

#エクスパンダ
# expander1 = st.expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')