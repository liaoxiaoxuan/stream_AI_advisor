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

print(df)