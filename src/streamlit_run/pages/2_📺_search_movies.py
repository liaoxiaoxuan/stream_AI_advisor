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

        # 側邊欄篩選器
        st.sidebar.header('篩選條件')  # 設定側邊欄的篩選條件標題

        # print(dataframe)




if __name__ == '__main__':
    main()