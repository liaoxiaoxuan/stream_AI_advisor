import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error  # 引入MySQL連接器中的Error類，用於處理錯誤
from dotenv import load_dotenv



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