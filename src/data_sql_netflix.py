import csv
import mysql.connector  # 匯入與MySQL互動所需的模組
from dotenv import load_dotenv
import os



# 載入 .env 檔案中的環境變數
load_dotenv()



# 匯入 CSV 到第一個 MySQL 資料庫
def import_csv_to_db_1(csv_file_path):
    # 從 .env 讀取資料庫 Netflix 的連接資訊
    host = os.getenv("MYSQL_HOST_N")
    user = os.getenv("MYSQL_USER_N")
    password = os.getenv("MYSQL_PASSWORD_N")
    database = os.getenv("MYSQL_DATABASE_N")