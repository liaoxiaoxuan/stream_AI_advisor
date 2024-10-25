import time

import streamlit as st

import numpy as np
import pandas as pd

import os
from PIL import Image



# 設置頁面標題與文字
st.title('串流影音平台推薦系統')
st.subheader("Streaming Media Platform Recommendation System")
st.write('幫助您在 Netflix 與 Disney+ 之間，作出最適切的選擇！')



# from chart_view import chart_view_page
# from search_movies import search_movies_page
# from match_rate import match_rate_page



# 測試從local上傳圖片
# 設定圖片文件夾路徑
image = Image.open(r".\reports\collect_data\cat_choose.png")
st.image(image)
# st.image(image, caption="串接💝")
# # 獲取圖片文件夾中所有圖片文件的路徑
# image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".jpg")]
# # 批量讀取圖片並進行處理
# for image_path in image_paths:
    # with Image.open(image_path) as img:
        # # 進行圖片處理，例如調整大小、裁剪等
        # img = img.resize((5184, 3456))
        # # 顯示圖片
        # img.show()
