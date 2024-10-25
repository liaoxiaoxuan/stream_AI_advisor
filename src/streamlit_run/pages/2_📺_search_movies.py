import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error  # 引入MySQL連接器中的Error類，用於處理錯誤

from dotenv import load_dotenv
import os



# 載入 .env 檔案中的環境變數
load_dotenv()



# 連接到MySQL數據庫
def create_connection(db_config):
    connection = None
    try:
        # 使用提供的配置參數連接到MySQL數據庫
        connection = mysql.connector.connect(**db_config)
        print(f"Successfully connected to MySQL database: {db_config['database']}")
    except Error as e:
        # 如果發生錯誤，輸出錯誤訊息
        print(f"The error '{e}' occurred")
    return connection  # 返回連接物件



# 從數據庫獲取數據
def get_data(connection, table):
    # 從指定的數據表中選取相關的數據字段
    query = f"SELECT type, title, director, cast, country, release_year, rating, duration, listed_in, description, keywords FROM {table}"
    return pd.read_sql(query, connection)  # 使用Pandas的read_sql方法執行查詢，並返回數據框



# 主函數
def main():
    st.title('搜尋 Netflix 和 Disney+ 的電影')  # 設定應用程式的標題
    st.subheader('Searching Movies on Netflix and Disney+')
    st.write(
        """
        請從左側欄位選擇篩選條件
        """)

    # 數據庫配置
    netflix_database_config = {  # Netflix資料庫的連接配置

        # 'host': 'your_netflix_host',
        # 'database': 'netflix_database',
        # 'user': 'your_netflix_username',
        # 'password': 'your_netflix_password'

        'host' : os.getenv('MYSQL_HOST_N'),
        'user' : os.getenv('MYSQL_USER_N'),
        'password' : os.getenv('MYSQL_PASSWORD_N'),
        'database' : os.getenv('MYSQL_DATABASE_N')

    }

    disney_database_config = {  # Disney+資料庫的連接配置
        # 'host': 'your_disney_host',
        # 'database': 'disney_database',
        # 'user': 'your_disney_username',
        # 'password': 'your_disney_password'

        'host' : os.getenv('MYSQL_HOST_D'),
        'user' : os.getenv('MYSQL_USER_D'),
        'password' : os.getenv('MYSQL_PASSWORD_D'),
        'database' : os.getenv('MYSQL_DATABASE_D')

    }

    # 創建數據庫連接
    netflix_connection = create_connection(netflix_database_config)  # 連接Netflix資料庫
    disney_connection = create_connection(disney_database_config)  # 連接Disney+資料庫

    if netflix_connection is not None and disney_connection is not None:  # 確認兩個資料庫的連接是否成功
        # 獲取Netflix和Disney+的數據
        netflix_dataframe = get_data(netflix_connection, 'data_netflix')  # 從Netflix資料庫獲取數據
        disney_dataframe = get_data(disney_connection, 'data_disney_plus')  # 從Disney+資料庫獲取數據

        # 添加來源列
        netflix_dataframe['source'] = 'Netflix'  # 在Netflix數據集中添加一列，用於標識來源
        disney_dataframe['source'] = 'Disney+'  # 在Disney+數據集中添加一列，用於標識來源

        # 合併數據集
        dataframe = pd.concat([netflix_dataframe, disney_dataframe], ignore_index=True)  # 合併兩個數據集


        # 建立篩選器
        
        # 側邊欄篩選器
        st.sidebar.header(' 🔎 篩選條件')  # 設定側邊欄的篩選條件標題

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
        
        # 顯示columns
        display_columns = ['type', 'title', 'director', 'cast', 'country', 'release_year', 'rating', 'duration', 'listed_in', 'description']
        
        # 分別顯示Netflix和Disney+的結果
        st.subheader(" 🍿 Netflix 搜尋結果：")
        netflix_results = filtered_dataframe[filtered_dataframe['source'] == 'Netflix'][display_columns]
        netflix_count = len(netflix_results)

        if netflix_count > 0:
            st.write(f"+ 共 {netflix_count} 筆符合條件的結果")
            st.dataframe(netflix_results)
        else:
            st.write("您所設定的條件，無相符的資料")

        # st.dataframe(netflix_results)
        
        st.subheader(" 🍿 Disney+ 搜尋結果：")
        disney_results = filtered_dataframe[filtered_dataframe['source'] == 'Disney+'][display_columns]

        disney_count = len(disney_results)
        
        if disney_count > 0:
            st.write(f"+ 共 {disney_count} 筆符合條件的結果")
            st.dataframe(disney_results)
        else:
            st.write("您所設定的條件，無相符的資料")

        # st.dataframe(disney_results)
        
        netflix_connection.close()
        disney_connection.close()
    else:
        st.error('無法連接到一個或多個數據庫')




if __name__ == '__main__':
    main()