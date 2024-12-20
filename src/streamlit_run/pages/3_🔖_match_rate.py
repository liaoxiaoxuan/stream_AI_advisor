import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import pandas as pd
# import mysql.connector
# from mysql.connector import Error  # 引入MySQL連接器中的Error類，用於處理錯誤

import sqlite3
from sqlite3 import Error

# from dotenv import load_dotenv
import os



# # 載入 .env 檔案中的環境變數
# load_dotenv()



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



# 顯示所選擇的篩選條件
def display_filter_summary(filters):
    st.markdown("### 📋 已選擇的篩選條件")  # 顯示標題
    
    # 創建一個風格化的容器來顯示篩選條件
    with st.container():
        for filter_name, filter_value in filters.items():
            if filter_value:  # 只顯示有被選擇的條件
                if isinstance(filter_value, tuple):  # 範圍型篩選條件
                    st.markdown(f"**{filter_name}:** {filter_value[0]} 到 {filter_value[1]}")  # 顯示範圍
                elif isinstance(filter_value, list):  # 多選篩選條件
                    if filter_value:  # 確保列表不為空
                        st.markdown(f"**{filter_name}:** {', '.join(map(str, filter_value))}")  # 顯示選擇的項目
                else:  # 單選篩選條件
                    st.markdown(f"**{filter_name}:** {filter_value}")  # 顯示選擇的值



# 計算符合條件的資料百分比
def calculate_match_percentage(original_df, filtered_df, platform):
    original_count = len(original_df[original_df['source'] == platform])  # 計算原始數據中該平台的數量
    filtered_count = len(filtered_df[filtered_df['source'] == platform])  # 計算過濾後數據中該平台的數量
    return (filtered_count / original_count * 100) if original_count > 0 else 0  # 計算百分比，避免除以0



# # 連接到MySQL數據庫
# def create_connection(db_config):
    # connection = None
    # try:
        # # 使用提供的配置參數連接到MySQL數據庫
        # connection = mysql.connector.connect(**db_config)
        # print(f"Successfully connected to MySQL database: {db_config['database']}")
    # except Error as e:
        # # 如果發生錯誤，輸出錯誤訊息
        # print(f"The error '{e}' occurred")
    # return connection  # 返回連接物件


# 連接到SQLite數據庫
def create_connection(db_file):
    connection = None
    try:
        # 使用提供的數據庫文件連接到SQLite數據庫
        connection = sqlite3.connect(db_file)
        print(f"Successfully connected to SQLite database: {db_file}")
    except Error as e:
        # 如果發生錯誤，輸出錯誤訊息
        print(f"The error '{e}' occurred")
    return connection  # 返回連接物件



# 從數據庫獲取數據
def get_data(connection, table):
    # 從指定的數據表中選取相關的數據字段
    query = f'SELECT "type", "title", "director", "cast", "country", "release_year", "rating", "duration", "listed_in", "description", "keywords" FROM "{table}"'
    return pd.read_sql(query, connection)  # 使用Pandas的read_sql方法執行查詢，並返回數據框



# 主函數
def main():
    st.title('Netflix 和 Disney+ 的推薦度比較')  # 設定應用程式的標題
    st.subheader('Recommendation Ratio of Netflix and Disney+')
    st.write(
        """
        - 請從左側欄位選擇篩選條件
        """)

    # # 數據庫配置
    # netflix_database_config = {  # Netflix資料庫的連接配置

        # # 'host': 'your_netflix_host',
        # # 'database': 'netflix_database',
        # # 'user': 'your_netflix_username',
        # # 'password': 'your_netflix_password'

        # 'host' : os.getenv('MYSQL_HOST_N'),
        # 'user' : os.getenv('MYSQL_USER_N'),
        # 'password' : os.getenv('MYSQL_PASSWORD_N'),
        # 'database' : os.getenv('MYSQL_DATABASE_N')

    # }

    # disney_database_config = {  # Disney+資料庫的連接配置
        # # 'host': 'your_disney_host',
        # # 'database': 'disney_database',
        # # 'user': 'your_disney_username',
        # # 'password': 'your_disney_password'

        # 'host' : os.getenv('MYSQL_HOST_D'),
        # 'user' : os.getenv('MYSQL_USER_D'),
        # 'password' : os.getenv('MYSQL_PASSWORD_D'),
        # 'database' : os.getenv('MYSQL_DATABASE_D')

    # }

    netflix_database_file = r"/mount/src/stream_ai_advisor/data/data_SQLite/netflix.db"  # Netflix資料庫文件的路徑
    disney_database_file = r"/mount/src/stream_ai_advisor/data/data_SQLite/disney.db"  # Disney+資料庫文件的路徑


    # 創建數據庫連接
    netflix_connection = create_connection(netflix_database_file)  # 連接Netflix資料庫
    disney_connection = create_connection(disney_database_file)  # 連接Disney+資料庫


    if netflix_connection is not None and disney_connection is not None:  # 確認兩個資料庫的連接是否成功
        # 獲取Netflix和Disney+的數據
        netflix_dataframe = get_data(netflix_connection, 'netflix_titles')  # 從Netflix資料庫獲取數據
        disney_dataframe = get_data(disney_connection, 'Disney_titles')  # 從Disney+資料庫獲取數據

        # 添加來源列
        netflix_dataframe['source'] = 'Netflix'  # 在Netflix數據集中添加一列，用於標識來源
        disney_dataframe['source'] = 'Disney+'  # 在Disney+數據集中添加一列，用於標識來源

        # 合併數據集
        dataframe = pd.concat([netflix_dataframe, disney_dataframe], ignore_index=True)  # 合併兩個數據集


        # 建立篩選器
        
        # 側邊欄篩選器
        st.sidebar.header(' ☑️ 選擇條件')  # 設定側邊欄的篩選條件標題

        # Type篩選器
        type_filter = st.sidebar.multiselect('選擇類型', sorted(dataframe['type'].unique()))  # 根據電影／影集類型篩選

        # 將需要排序的選項列表準備好
        titles = sorted(dataframe['title'].unique())
        directors = sorted(dataframe['director'].dropna().str.strip().str.strip('"').str.split(',').explode().str.strip().unique())
        cast_list = sorted(dataframe['cast'].dropna().str.strip().str.strip('"').str.split(',').explode().str.strip().unique())
        countries = sorted(dataframe['country'].dropna().str.strip().str.strip('"').str.split(',').explode().str.strip().unique())
        ratings = sorted(dataframe['rating'].dropna().unique())
        categories = sorted(dataframe['listed_in'].dropna().str.strip().str.strip('"').str.split(',').explode().str.strip().unique())
        keywords = sorted(dataframe['keywords'].dropna().str.strip().str.strip('"').str.split(',').explode().str.strip().unique())

        # Title篩選器
        title_filter = st.sidebar.selectbox('搜尋電影名稱', [''] + list(titles))  # 根據標題關鍵字篩選
        # Director篩選器
        director_filter = st.sidebar.selectbox('搜尋導演名字', [''] + list(directors))  # 根據導演名字篩選
        # Cast篩選器
        cast_filter = st.sidebar.selectbox('搜尋演員名字', [''] + list(cast_list))  # 根據演員名字篩選
        # Country篩選器
        country_filter = st.sidebar.multiselect('選擇發行國家', countries)  # 根據國家篩選
        # Release Year篩選器
        min_year, max_year = int(dataframe['release_year'].min()), int(dataframe['release_year'].max())  # 獲取年份範圍
        year_range = st.sidebar.slider('選擇發行年份範圍', min_year, max_year, (min_year, max_year))  # 根據發行年份篩選
        # Rating篩選器
        rating_filter = st.sidebar.multiselect('選擇分級', ratings)  # 根據電影／影集的分級篩選
        # Duration篩選器
        if 'Movie' in type_filter:
            min_duration = int(dataframe[dataframe['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float).min())
            max_duration = int(dataframe[dataframe['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float).max())
            duration_range = st.sidebar.slider('選擇電影時長 (分鐘)', min_duration, max_duration, (min_duration, max_duration))
        elif 'TV Show' in type_filter:
            min_seasons = int(dataframe[dataframe['type'] == 'TV Show']['duration'].str.extract('(\d+)').astype(float).min())
            max_seasons = int(dataframe[dataframe['type'] == 'TV Show']['duration'].str.extract('(\d+)').astype(float).max())
            duration_range = st.sidebar.slider('選擇季數', min_seasons, max_seasons, (min_seasons, max_seasons))
        # Listed In篩選器
        listed_in_filter = st.sidebar.multiselect('選擇類別', categories)  # 根據類別篩選
        # Description (Keywords) 篩選器
        keywords_filter = st.sidebar.selectbox('搜尋電影關鍵字', [''] + list(keywords))  # 根據關鍵字篩選


        # 應用篩選器
        filtered_dataframe = dataframe.copy()
        
        if type_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['type'].isin(type_filter)]
        
        if title_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['title'] == title_filter]
        
        if director_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['director'] == director_filter]
        
        if cast_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['cast'].str.contains(cast_filter, case=False, na=False)]
        
        if country_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['country'].apply(lambda x: any(country in str(x) for country in country_filter))]
        
        filtered_dataframe = filtered_dataframe[(filtered_dataframe['release_year'] >= year_range[0]) & (filtered_dataframe['release_year'] <= year_range[1])]
        
        if rating_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['rating'].isin(rating_filter)]
        
        # 更新後的duration篩選邏輯
        if 'Movie' in type_filter:
            filtered_dataframe['duration_num'] = filtered_dataframe['duration'].str.extract('(\d+)').astype(float)
            filtered_dataframe = filtered_dataframe[
                (filtered_dataframe['duration_num'] >= duration_range[0]) & 
                (filtered_dataframe['duration_num'] <= duration_range[1])
            ]
        elif 'TV Show' in type_filter:
            filtered_dataframe['seasons'] = filtered_dataframe['duration'].str.extract('(\d+)').astype(float)
            filtered_dataframe = filtered_dataframe[
                (filtered_dataframe['seasons'] >= duration_range[0]) & 
                (filtered_dataframe['seasons'] <= duration_range[1])
            ]
        
        if listed_in_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['listed_in'].apply(lambda x: any(category in x for category in listed_in_filter))]
        
        if keywords_filter:
            filtered_dataframe = filtered_dataframe[filtered_dataframe['keywords'].str.contains(keywords_filter, case=False, na=False)]
    
    # 收集所有篩選條件
    filters = {
        '類型': type_filter if type_filter else None,  # 收集類型篩選
        '電影名稱': title_filter if title_filter else None,  # 收集電影名稱篩選
        '導演': director_filter if director_filter else None,  # 收集導演篩選
        '演員': cast_filter if cast_filter else None,  # 收集演員篩選
        '發行國家': country_filter if country_filter else None,  # 收集發行國家篩選
        '發行年份': year_range,  # 收集發行年份篩選
        '分級': rating_filter if rating_filter else None,  # 收集分級篩選
        '類別': listed_in_filter if listed_in_filter else None,  # 收集類別篩選
        '關鍵字': keywords_filter if keywords_filter else None  # 收集關鍵字篩選
    }
    
    # 添加時長/季數篩選條件
    if type_filter:  # 如果有類型篩選
        if 'Movie' in type_filter:  # 如果類型包含電影
            filters['電影時長 (分鐘)'] = duration_range  # 設置電影時長篩選
        elif 'TV Show' in type_filter:  # 如果類型包含電視劇
            filters['季數'] = duration_range  # 設置季數篩選

    # 顯示篩選條件摘要
    display_filter_summary({k: v for k, v in filters.items() if v})  # 顯示已選擇的篩選條件
    
    # 計算匹配百分比
    netflix_percentage = calculate_match_percentage(dataframe, filtered_dataframe, 'Netflix')  # 計算Netflix的符合條件百分比
    disney_percentage = calculate_match_percentage(dataframe, filtered_dataframe, 'Disney+')  # 計算Disney+的符合條件百分比
    
    # 顯示匹配結果和統計圖表
    st.markdown("### 🧩 匹配指數")  # 顯示統計標題
    
    # 使用columns布局來並排顯示兩個圖表
    col1, col2 = st.columns(2)  # 創建兩列以並排顯示圖表
    
    with col1:
        # Netflix環形圖
        netflix_fig = create_gradient_donut(
            start_color=(229/255, 6/255, 19/255),  # Netflix 紅
            end_color=(0, 0, 0),                   # 黑色
            match_percentage=netflix_percentage,  # 設定符合條件的百分比
            platform_name='Netflix'  # 設定平台名稱
        )
        st.pyplot(netflix_fig)  # 在Streamlit中顯示Netflix環形圖
        
    with col2:
        # Disney+環形圖
        disney_fig = create_gradient_donut(
            start_color=(104/255, 212/255, 212/255),     # Disney+ 深藍
            end_color=(0/255, 32/255, 52/255),   # Disney+ 淺藍綠
            match_percentage=disney_percentage,  # 設定符合條件的百分比
            platform_name='Disney+'  # 設定平台名稱
        )
        st.pyplot(disney_fig)  # 在Streamlit中顯示Disney+環形圖



# 啟動應用
if __name__ == "__main__":
    main()  # 執行主函數