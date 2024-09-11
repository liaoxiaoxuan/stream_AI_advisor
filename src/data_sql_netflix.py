import csv
import mysql.connector  # 匯入與MySQL互動所需的模組
from dotenv import load_dotenv
import os



# 載入 .env 檔案中的環境變數
load_dotenv()



# 定義 CSV 數據文件路徑

csv_file_path = os.path.join('data', 'processed', 'netflix_titles_processed.csv')

# 匯入 CSV 到第一個 MySQL 資料庫
def import_csv_to_db_1(csv_file_path):
    # 從 .env 讀取資料庫 Netflix 的連接資訊
    host = os.getenv("MYSQL_HOST_N")
    user = os.getenv("MYSQL_USER_N")
    password = os.getenv("MYSQL_PASSWORD_N")
    database = os.getenv("MYSQL_DATABASE_N")

    # 連接到 MySQL Netflix 資料庫
    db_connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # 創建一個資料庫游標
    db_cursor = db_connection.cursor()

    # 建立表格
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS netflix_titles (
        show_id VARCHAR(255) PRIMARY KEY,  # 設定 show_id 為主鍵
        type VARCHAR(50),
        title VARCHAR(255),
        director VARCHAR(255),
        cast TEXT,
        country VARCHAR(255),
        date_added VARCHAR(50),
        release_year INT,
        rating VARCHAR(50),
        duration VARCHAR(50),
        listed_in TEXT,
        description TEXT
    """)


