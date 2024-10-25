import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap



# 創建漸變環形圖
def create_gradient_donut(start_color, end_color, match_percentage, platform_name):

    # 定義數據
    符合條件_資料總和 = match_percentage  # 設定符合條件的百分比
    所有資料 = 100 - 符合條件_資料總和  # 計算不符合條件的百分比
    
    # 將符合條件的部分分成多個小段以實現平滑漸變
    n_segments = 1000  # 設定漸變的段數
    segment_size = 符合條件_資料總和 / n_segments  # 每個小段的大小
    segments = [segment_size] * n_segments  # 創建小段列表
    segments.append(所有資料)  # 將不符合條件的部分添加到列表

    # 創建漸變色
    colors = []  # 初始化顏色列表
    for i in range(n_segments):
        # 計算當前小段的顏色
        ratio = i / (n_segments - 1)  # 計算比例
        color = tuple(a + (b - a) * ratio for a, b in zip(start_color, end_color))  # 根據比例計算顏色
        colors.append(color)  # 將顏色添加到顏色列表