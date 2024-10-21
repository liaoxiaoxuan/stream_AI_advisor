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
    st.title('Netflix 和 Disney+ 篩選電影')  # 設定應用程式的標題

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
        st.sidebar.header('篩選條件')  # 設定側邊欄的篩選條件標題

        # Type篩選器
        type_filter = st.sidebar.multiselect('選擇類型', options=dataframe['type'].unique())  # 根據電影／影集類型篩選
        # Title篩選器
        title_filter = st.sidebar.text_input('輸入標題關鍵字')  # 根據標題關鍵字篩選
        # Director篩選器
        director_filter = st.sidebar.text_input('輸入導演名字')  # 根據導演名字篩選
        # Cast篩選器
        cast_filter = st.sidebar.text_input('輸入演員名字')  # 根據演員名字篩選
        # Country篩選器
        country_filter = st.sidebar.multiselect('選擇國家', options=dataframe['country'].str.split(', ').explode().unique())  # 根據國家篩選
        # Release Year篩選器
        min_year, max_year = int(dataframe['release_year'].min()), int(dataframe['release_year'].max())  # 獲取年份範圍
        year_range = st.sidebar.slider('選擇發行年份範圍', min_year, max_year, (min_year, max_year))  # 根據發行年份篩選
        # Rating篩選器
        rating_filter = st.sidebar.multiselect('選擇分級', options=dataframe['rating'].unique())  # 根據電影／影集的分級篩選
        # Duration篩選器
        if 'Movie' in type_filter:  # 如果篩選器中選擇的是電影
            duration_bins = [10,20,40,60,90,120,150,180,240,300,330]  # 定義電影時長範圍
            duration_labels = [f"{duration_bins[i]}-{duration_bins[i+1]} min" for i in range(len(duration_bins)-1)]  # 生成對應的時長標籤
            duration_filter = st.sidebar.multiselect('選擇電影時長', options=duration_labels)  # 根據時長篩選
        elif 'TV Show' in type_filter:  # 如果篩選器中選擇的是影集
            season_bins = [1,2,3,5,7,9,11,13,15,17,19]  # 定義影集季數範圍
            season_labels = [f"{season_bins[i]}-{season_bins[i+1]} seasons" for i in range(len(season_bins)-1)]  # 生成對應的季數標籤
            duration_filter = st.sidebar.multiselect('選擇季數', options=season_labels)  # 根據季數篩選
        # Listed In篩選器
        listed_in_filter = st.sidebar.multiselect('選擇類別', options=dataframe['listed_in'].str.split(', ').explode().unique())  # 根據類別篩選
        # Description (Keywords) 篩選器
        keywords_filter = st.sidebar.multiselect('輸入關鍵字')  # 根據關鍵字篩選


        # 應用篩選器
        filtered_dataframe = dataframe.copy()  # 複製數據集，避免修改原數據
        
        if type_filter:  # 應用類型篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['type'].isin(type_filter)]
        
        if title_filter:  # 應用標題篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['title'].str.contains(title_filter, case=False)]
        
        if director_filter:  # 應用導演篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['director'].str.contains(director_filter, case=False)]
        
        if cast_filter:  # 應用演員篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['cast'].str.contains(cast_filter, case=False)]
        
        if country_filter:  # 應用國家篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['country'].apply(lambda x: any(country in x for country in country_filter))]
        
        # 應用發行年份篩選
        filtered_dataframe = filtered_dataframe[(filtered_dataframe['release_year'] >= year_range[0]) & (filtered_dataframe['release_year'] <= year_range[1])]
        
        if rating_filter:  # 應用分級篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['rating'].isin(rating_filter)]
        
        if duration_filter:  # 應用時長或季數篩選
            if 'Movie' in type_filter:  # 如果篩選的是電影
                filtered_dataframe['duration_num'] = filtered_dataframe['duration'].str.extract('(\d+)').astype(float)  # 提取時長數字
                for duration_range in duration_filter:
                    min_duration, max_duration = map(int, duration_range.split('-')[0].split()[0]), int(duration_range.split('-')[1].split()[0])
                    filtered_dataframe = filtered_dataframe[(filtered_dataframe['duration_num'] >= min_duration) & (filtered_dataframe['duration_num'] < max_duration)]
            elif 'TV Show' in type_filter:  # 如果篩選的是影集
                filtered_dataframe['seasons'] = filtered_dataframe['duration'].str.extract('(\d+)').astype(float)  # 提取季數數字
                for season_range in duration_filter:
                    min_season, max_season = map(int, season_range.split('-')[0].split()[0]), int(season_range.split('-')[1].split()[0])
                    filtered_dataframe = filtered_dataframe[(filtered_dataframe['seasons'] >= min_season) & (filtered_dataframe['seasons'] < max_season)]
        
        if listed_in_filter:  # 應用類別篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['listed_in'].apply(lambda x: any(category in x for category in listed_in_filter))]
        
        if keywords_filter:  # 應用關鍵字篩選
            filtered_dataframe = filtered_dataframe[filtered_dataframe['description'].str.contains(keywords_filter, case=False)]
        
        # 顯示篩選後的結果
        st.write(f"共找到 {len(filtered_dataframe)} 條結果")  # 顯示結果數量
        st.dataframe(filtered_dataframe)  # 顯示篩選後的數據集

        # print(dataframe)




if __name__ == '__main__':
    main()