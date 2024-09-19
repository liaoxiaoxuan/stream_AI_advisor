import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os


# 載入 .env 檔案中的環境變數

load_dotenv()


# 初始化資料庫連接，使用 .env 檔案中的環境變數或傳入的參數

class MySQLConnector:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host if host else os.getenv('MYSQL_HOST_N')
        self.user = user if user else os.getenv('MYSQL_USER_N')
        self.password = password if password else os.getenv('MYSQL_PASSWORD_N')
        self.database = database if database else os.getenv('MYSQL_DATABASE_N')
        self.conn = None
        self.cursor = None


# 連接到 MySQL 資料庫

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("成功連接到資料庫")
        except mysql.connector.Error as err:
            print(f"資料庫連接失敗: {err}")


# 執行 SQL 查詢，返回 pandas DataFrame

    def query(self, sql_query):
        try:
            self.cursor.execute(sql_query)
            result = self.cursor.fetchall()
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(result, columns=columns)
            return df
        except mysql.connector.Error as err:
            print(f"執行查詢時出現錯誤: {err}")
            return None


# 執行 SQL 查詢，僅返回指定欄位的資料

    def query_specific_columns(self, table_name, columns):
        
        # param table_name：資料表名稱 ex: "data_netflix"
        # param columns：欲查詢的欄位名稱列表 ex: "title"
        # return：pandas DataFrame
        
        columns_str = ', '.join(columns)  # 將欄位名稱列表轉換為 SQL 查詢所需的格式
        sql_query = f"SELECT {columns_str} FROM {table_name}"  # 构造 SQL 查詢語句
        return self.query(sql_query)  # 使用已存在的 query 方法執行查詢


# 關閉游標和資料庫連接

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("資料庫連接已關閉")



if __name__ == "__main__":
    db = MySQLConnector()
    db.connect()

    # 查詢特定欄位的資料
    table_name = "data_netflix"
    columns = ["title"]  # 替換成你需要的欄位名稱
    df = db.query_specific_columns(table_name, columns)

    if df is not None:
        print(df.head())  # 顯示前幾筆資料
    
    db.close()