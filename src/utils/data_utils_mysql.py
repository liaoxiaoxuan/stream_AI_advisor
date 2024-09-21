import pandas as pd
import os

import mysql.connector
from dotenv import load_dotenv

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# from data_utils_mysql import MySQLConnector



# 載入 .env 檔案中的環境變數

load_dotenv()


# 初始化資料庫連接，使用 .env 檔案中的環境變數或傳入的參數

class MySQLConnector:
    def __init__(self, host=None, user=None, password=None, database=None,name='N'):
        self.host = host if host else os.getenv(f'MYSQL_HOST_{name}')
        self.user = user if user else os.getenv(f'MYSQL_USER_{name}')
        self.password = password if password else os.getenv(f'MYSQL_PASSWORD_{name}')
        self.database = database if database else os.getenv(f'MYSQL_DATABASE_{name}')
        self.conn = None
        self.cursor = None


# 連接到 MySQL 資料庫
    def connect(self):
        """
        連接到 MySQL 資料庫
        """
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
        """
        執行 SQL 查詢，返回 pandas DataFrame
        """
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
        """
        執行 SQL 查詢，僅返回指定欄位的資料
        """
        # param table_name：資料表名稱 ex: "data_netflix"
        # param columns：欲查詢的欄位名稱列表 ex: "title"
        # return：pandas DataFrame
        
        columns_str = ', '.join(columns)  # 將欄位名稱列表轉換為 SQL 查詢所需的格式
        sql_query = f"SELECT {columns_str} FROM {table_name}"  # 建構 SQL 查詢語句
        return self.query(sql_query)  # 使用已存在的 query 方法執行查詢


    # 獲取表的所有列名
    def get_table_columns(self, table_name):
        """
        獲取表的所有列名
        """
        try:
            self.cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = [column[0] for column in self.cursor.fetchall()]
            return columns
        except mysql.connector.Error as err:
            print(f"獲取表結構時出現錯誤: {err}")
            return None


# 關閉游標和資料庫連接
    def close(self):
        """
        關閉游標和資料庫連接
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("資料庫連接已關閉")


class Analysis:
    def __init__(self, table_name, db_name='N'):
        # 初始化 MySQLConnector 實例，用於數據庫連接
        self.db = MySQLConnector(name=db_name)
        # 設置要分析的資料表名稱
        self.table_name = table_name
        # 初始化 data 屬性為 None，稍後會用來存儲從數據庫讀取的數據
        self.data = None


    # 從 MySQL 資料庫讀取資料
    def get_data(self):
        """
        從 MySQL 資料庫讀取資料
        """
        # 連接到數據庫
        self.db.connect()
        # 獲取指定表的所有列名
        columns = self.db.get_table_columns(self.table_name)
        # 查詢所有列的數據並存儲到 self.data
        self.data = self.db.query_specific_columns(self.table_name, columns)
        # 關閉數據庫連接
        self.db.close()
        # 返回讀取的數據
        return self.data


    # 計算資料，根據需求進行各種統計分析
    def calculate(self):
        """
        計算資料，根據需求進行各種統計分析
        """
        # 檢查是否已經加載了數據
        if self.data is None:
            raise ValueError("Data not loaded. Call get_data() first.")

        # 計算內容類型的數量
        self.type_counts = self.data['type'].value_counts()
        # 將 'date_added' 列轉換為日期時間格式
        self.data['date_added'] = pd.to_datetime(self.data['date_added'])
        # 從 'date_added' 提取年份
        self.data['year'] = self.data['date_added'].dt.year
        # 從 'date_added' 提取月份名稱
        self.data['month'] = self.data['date_added'].dt.month_name()
        # 計算每年每月的內容數量
        self.month_counts = self.data.groupby('year')['month'].value_counts()
        # 計算每年的內容數量並按年份排序
        self.year_counts = self.data['year'].value_counts().sort_index()
        # 計算每個發行年份的內容數量並排序
        self.release_year_counts = self.data['release_year'].value_counts().sort_index()
        # 計算每個分級的內容數量並排序
        self.rating_counts = self.data['rating'].value_counts().sort_index()


    # 根據指定的圖表類型和資料類型進行可視化
    def visualize(self, plot_type, data_type):
        """
        根據指定的圖表類型和資料類型進行可視化
        """
        if plot_type == 'bar':
            if data_type == 'type':
                # 繪製內容類型的柱狀圖
                self._plot_bar(self.type_counts, 'Content Type Distribution')
            elif data_type == 'rating':
                # 繪製內容分級的柱狀圖
                self._plot_bar(self.rating_counts, 'Content Rating Distribution')
        elif plot_type == 'pie':
            if data_type == 'type':
                # 繪製內容類型的圓餅圖
                self._plot_pie(self.type_counts, 'Content Type Distribution')
            elif data_type == 'rating':
                # 繪製內容分級的圓餅圖
                self._plot_pie(self.rating_counts, 'Content Rating Distribution')
        elif plot_type == 'heatmap':
            if data_type == 'month_year':
                # 繪製年月內容數量的熱力圖
                self._plot_heatmap()
        elif plot_type == 'line':
            if data_type == 'year':
                # 繪製年度內容數量的折線圖
                self._plot_line(self.year_counts, 'Yearly Content Addition')

    def _plot_bar(self, data, title):
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(12, 6))
        # 使用 Seaborn 繪製柱狀圖
        sns.barplot(x=data.index, y=data.values)
        # 設置圖表標題
        plt.title(title)
        # 旋轉 x 軸標籤，避免重疊
        plt.xticks(rotation=45)
        # 自動調整子圖參數，使之填充整個圖像區域
        plt.tight_layout()

    def _plot_pie(self, data, title):
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(10, 10))
        # 繪製圓餅圖
        plt.pie(data.values, labels=data.index, autopct='%1.1f%%')
        # 設置圖表標題
        plt.title(title)

    def _plot_heatmap(self):
        # 將月度數據轉換為透視表格式
        pivot_table = self.month_counts.unstack()
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(12, 8))
        # 使用 Seaborn 繪製熱力圖
        sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu')
        # 設置圖表標題
        plt.title('Content Addition Heatmap by Year and Month')

    def _plot_line(self, data, title):
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(12, 6))
        # 繪製折線圖
        plt.plot(data.index, data.values)
        # 設置圖表標題
        plt.title(title)
        # 設置 x 軸標籤
        plt.xlabel('Year')
        # 設置 y 軸標籤
        plt.ylabel('Number of Contents')

    
    # 儲存當前的圖表
    def export(self, filename):
        """
        儲存當前的圖表
        """
        # 設置輸出目錄
        # output_dir = os.path.join('D:\PYTHON\oo_hank_project\stream_AI_advisor\reports\collect_data')
        output_dir = os.path.join('reports', 'figures')
        # 創建輸出目錄（如果不存在）
        os.makedirs(output_dir, exist_ok=True)
        # 保存圖表到指定文件
        plt.savefig(os.path.join(output_dir, filename))
        # 關閉當前圖表，釋放內存
        plt.close()


def mySQLConnector():
    db = MySQLConnector(name="N")
    db.connect()

    # 查詢特定欄位的資料
    table_name = "data_netflix"
    # columns = ["type"]  # 替換成你需要的欄位名稱
    # df = db.query_specific_columns(table_name, columns)

    # 動態獲取表的所有列名
    all_columns = db.get_table_columns(table_name)

    if all_columns:
        print(f"表 {table_name} 的所有列: {', '.join(all_columns)}")

        # 使用for循環遍歷所有列
        for column in all_columns:
            print(f"\n查詢列: {column}")
            df = db.query_specific_columns(table_name, [column])
            if df is not None:
                print(df.head())  # 顯示前幾筆資料
            else:
                print(f"查詢 {column} 列時出現錯誤")
    else:
        print(f"無法獲取表 {table_name} 的列訊息")

    db.close()

    # if df is not None:
    #     print(df.head())  # 顯示前幾筆資料
    
    # db.close()

def analysis():
    # 創建 Analysis 實例，指定資料表名稱
    analysis = Analysis('data_netflix')
    # 從數據庫獲取數據
    analysis.get_data()
    # 進行數據計算
    analysis.calculate()

    # 生成並保存內容類型柱狀圖
    analysis.visualize('bar', 'type')
    analysis.export('content_type_bar.png')

    # 生成並保存內容分級圓餅圖
    analysis.visualize('pie', 'rating')
    analysis.export('content_rating_pie.png')

    # 生成並保存年月內容數量熱力圖
    analysis.visualize('heatmap', 'month_year')
    analysis.export('content_addition_heatmap.png')

    # 生成並保存年度內容數量折線圖
    analysis.visualize('line', 'year')
    analysis.export('yearly_content_addition_line.png')

def main():
    mySQLConnector()
    analysis()

if __name__ == "__main__":
    main()


