import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門') #タイトル

st.write('Display Image') #本文追加

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})           #データフレーム作成

st.write(df) #上記を表示
st.dataframe(df) #データフレーム作成
st.dataframe(df, width=100, height=100) #引数（幅）
st.dataframe(df.style.highlight_max(axis=0)) #ハイライト[最大の値列](列；0,行：1)

st.table(df.style.highlight_max(axis=0)) #table形式

# Magicコマンド(markdown記法)
"""
# 章S
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""


# chart(グラフ)
df = pd.DataFrame(
    np.random.rand(20, 3), #乱数値(20行,3列)
    columns=['a','b','c']
)           #データフレーム作成

st.line_chart(df) #折れ線グラフ
st.area_chart(df) #折れ線グラフ(範囲塗りつぶし)
st.bar_chart(df) #棒グラフ(範囲塗りつぶし)


# Map
df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70], #日本付近
    columns=['lat','lon'] #緯度と経度
)           #データフレーム作成
st.map(df)


# 画像
img = Image.open('510-1.jpg')
st.image(img, caption='ペンギン', use_column_width=True)