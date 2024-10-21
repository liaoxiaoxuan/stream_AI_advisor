import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error  # 引入MySQL連接器中的Error類，用於處理錯誤



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



