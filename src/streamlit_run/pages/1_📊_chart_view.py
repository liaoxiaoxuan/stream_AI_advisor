import streamlit as st

import numpy as np
import pandas as pd



# 分頁容器標籤
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
   ["說明", "影片類型", "導演", "演員", "製作國家", "上架日期", "年齡分級", "時長", "內容分類", "影片摘要"]
   )

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
