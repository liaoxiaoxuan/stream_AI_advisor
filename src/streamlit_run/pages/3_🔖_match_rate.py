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
    
    # 添加透明色給未填充部分
    colors.append((1, 1, 1, 0))  # 添加透明顏色
    
    # 設置圖表樣式
    plt.style.use('dark_background')  # 使用深色主題，配合Streamlit
    fig, ax = plt.subplots(figsize=(4, 4))  # 調整大小適應Streamlit側邊

    # 繪製環形圖
    wedges, texts, autotexts = ax.pie(
        segments,  # 環形圖的數據
        colors=colors,  # 環形圖的顏色
        startangle=90,  # 從90度開始繪製
        wedgeprops=dict(width=0.3),  # 設置環形圖的寬度
        autopct='',  # 不顯示自動標籤
    )
    
    # 中心添加百分比文字
    plt.text(0, 0, f'{符合條件_資料總和:.1f}%', ha='center', va='center', 
             fontsize=16, color=start_color, fontweight='bold')  # 在中心顯示符合條件的百分比
    
    plt.axis('equal')  # 確保環形圖比例正確
    plt.title(f'{platform_name}\n符合篩選條件比例', 
              pad=10, color='white', fontsize=12)  # 設置標題
    
    # 設置背景透明
    fig.patch.set_alpha(0.0)  # 圖表背景透明
    ax.patch.set_alpha(0.0)  # 圖形區域背景透明
    
    return fig  # 返回生成的圖表

