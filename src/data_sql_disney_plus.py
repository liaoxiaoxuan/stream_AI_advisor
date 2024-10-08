import pandas as pd
import csv
import mysql.connector  # 匯入與MySQL互動所需的模組
from dotenv import load_dotenv
import os
import pymysql



# 定義 CSV 數據文件路徑

csv_file_path = 'D:/PYTHON/oo_hank_project/stream_AI_advisor/data/processed/disney_plus_titles_processed.csv'
# csv_file_path = os.path.join('data', 'processed', 'netflix_titles_processed.csv')

# 讀取 csv 文件到 DataFrame

df = pd.read_csv(csv_file_path)



# 載入 .env 檔案中的環境變數
load_dotenv()

# 匯入 CSV 到第一個 MySQL 資料庫
def import_csv_to_db_D(csv_file_path):
    # 從 .env 讀取資料庫 Netflix 的連接資訊
    
    host = os.getenv("MYSQL_HOST_D")
    user = os.getenv("MYSQL_USER_D")
    password = os.getenv("MYSQL_PASSWORD_D")
    database = os.getenv("MYSQL_DATABASE_D")

    # print(f"Host: {host}, User: {user}, Password: {password}, Database: {database}")

    # 連接到 MySQL Disney= 資料庫
    db_connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    # 創建一個資料庫游標
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
    DROP TABLE IF EXISTS data_disney_plus;
    """)
    # return

    # 建立表格
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_Disney_plus (
        show_id VARCHAR(10) PRIMARY KEY,  # 設定 show_id 為主鍵
        type VARCHAR(10),
        title VARCHAR(250),
        director VARCHAR(500),
        cast VARCHAR(2000),
        country VARCHAR(200),
        date_added DATE,
        release_year INT,
        rating VARCHAR(50),
        duration VARCHAR(50),
        listed_in VARCHAR(100),
        description VARCHAR(800))
    """)

    # 打開 CSV 檔案
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        header = next(csv_data)  # 跳過標題行

        # 插入每一行數據
        for row in csv_data:
            db_cursor.execute(
                """INSERT INTO data_Disney_plus (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, row)
    
    # 提交更改並關閉連接
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    print("CSV 已成功匯入到 MySQL Disney+ 資料庫！")


if __name__ == "__main__":
    import_csv_to_db_D(csv_file_path)


# print(df)