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
        self.set_color_table()
        


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

        # 計算內容類型 'type' 的數量
        self.type_counts = self.data['type'].value_counts()
        
        # 分別計算 "TV Show" 和 "Movie" 的 year_counts
        self.TV_Show = self.data[self.data["type"] == "TV Show"]
        self.tv_show_date = self.TV_Show[['date_added']].dropna()  # 提取 "TV Show" 的 "date_added" 列，並刪除空值
        self.tv_show_date['date_added'] = pd.to_datetime(self.tv_show_date['date_added'], format='%Y/%m/%d')  # 確保 'date_added' 列是日期時間格式
        self.tv_show_date['year'] = self.tv_show_date['date_added'].dt.year  # 提取年份
        self.tv_show_year_counts = self.tv_show_date['year'].value_counts().sort_index()  # 計算每年 "TV Show" 的數量並排序
        
        self.Movie = self.data[self.data["type"] == "Movie"]
        self.movie_date = self.Movie[['date_added']].dropna()  # 提取 "Movie" 的 "date_added" 列，並刪除空值
        self.movie_date['date_added'] = pd.to_datetime(self.movie_date['date_added'], format='%Y/%m/%d')  # 確保 'date_added' 列是日期時間格式
        self.movie_date['year'] = self.movie_date['date_added'].dt.year  # 提取年份
        self.movie_year_counts = self.movie_date['year'].value_counts().sort_index()  # 計算每年 "Movie" 的數量並排序
        

        # 將 'date_added' 列轉換為日期時間格式
        self.data['date_added'] = pd.to_datetime(self.data['date_added'])
        # 從 'date_added' 提取年份
        self.data['year'] = self.data['date_added'].dt.year
        # 從 'date_added' 提取月份名稱
        self.data['month'] = self.data['date_added'].dt.month_name()
        # 指定月份的順序
        self.month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        # 將月份轉換為有序類別
        self.data['month'] = pd.Categorical(self.data['month'], categories=self.month_order, ordered=True)
        # 計算每年每月的新增數量
        self.month_counts = self.data.groupby('year')['month'].value_counts()
        # 計算每年的新增數量並按年份排序
        self.year_counts = self.data['year'].value_counts().sort_index()

        # 計算每個發行年份 'release_year' 的內容數量並排序
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
            if data_type == 'date_added':
                # 繪製年月內容數量的熱力圖
                self._plot_heatmap(self.month_counts, 'Content Addition Heatmap by Year and Month')
        
        elif plot_type == 'table':
            if data_type == 'date_added':
                # 繪製年度內容數量的折線圖
                self._plot_table(self.month_counts, 'Content Addition Table by Year and Month')
        
        elif plot_type == 'a_line':
            if data_type == 'year':
                # 繪製年度內容數量的折線圖
                self._plot_a_line(self.year_counts, 'Yearly Content Addition')
        
        elif plot_type == 'two_line':
            if data_type == 'year':
                # 繪製年度內容數量的折線圖
                self._plot_two_line(self.year_counts, 'Yearly Counts of TV Shows and Movies')

        elif plot_type == 'combine_b2l':
            if data_type == 'year':
                # 繪製年度內容數量的折線圖
                self._plot_combine_b2l(self.year_counts, 'Yearly Growth of TV Shows and Movies on Netflix')

    def set_color_table(self):
        self.colors_map = {
            'N1': ['#f9dbbd'],  # Netflix 單色
            'N2':  ['#E50611','#000000'],  # Netflix 雙色主視覺
        }

        self.color_map = {
            'N1': ['#f9dbbd'],  # Netflix 單色
            'N2':  ['#E50611','#000000'],  # Netflix 雙色主視覺
        }
    
    def _plot_bar(self, data, title):
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(12, 6))
        # 使用 Seaborn 繪製柱狀圖
        ax = sns.barplot(x=data.index, y=data.values)
        # 在每個柱狀圖上添加數字標籤
        for i, value in enumerate(data.values):
            ax.text(i, value + 0.01, f'{value:.0f}', ha='center', va='bottom')
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
        plt.pie(
            data.values, 
            labels=data.index, 
            colors=self.colors_map['N2'], 
            autopct='%1.1f%%', 
            textprops={'color': 'white', 'fontsize': 12, 'fontweight': 'bold'}
            )
        # 設置圖表標題
        plt.title(title)

    def _plot_heatmap(self, data, title):
        # 將月度數據轉換為透視表格式
        pivot_table = self.month_counts.unstack()
        # 創建一個新的圖形，設置大小
        plt.figure(figsize=(12, 8))
        # 使用 Seaborn 繪製熱力圖
        sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu')
        """
        設定熱力圖配色 cmap
        'YlGnBu': 黃-綠-藍漸變
        'viridis': 默認色彩映射，綠-藍-黃
        'coolwarm': 冷暖色對比
        'magma': 黑-紫-橙漸變
        """
        # 設置圖表標題
        plt.title('Content Addition Heatmap by Year and Month')

    def _plot_table(self, data, title):
        
        # 排列為矩陣
        matrix = self.month_counts.unstack()  # 先使用 unstack() 將月份從行索引轉為列索引，未出現的月份會變成 NaN
        matrix = matrix.fillna(0)  # 使用 fillna(0) 將 NaN 值填充為 0
        matrix = matrix.astype(int)  # 將數據類型轉換為整數
        matrix = matrix[self.month_order]  # 根據指定的月份順序重新排序列
        result = matrix.T  # 將矩陣轉置，讓年份成為列索引，月份成為行索引# 設置圖表大小和分辨率
        
        # 計算年和月的總和
        result['Month Total'] = result.sum(axis=1)  # 計算每年的總和，並將結果新增至 DataFrame 的新列 'Year Total'
        result.loc['Year Total'] = result.sum(axis=0)  # 計算每月的總和，並將結果新增至 DataFrame 的新行 'Month Total'

        # 繪製表格
        plt.figure(figsize=(12, 8), dpi=300)
        # plt.figure(): 創建一個新的圖形對象，這是 Matplotlib 用來顯示和處理圖形的容器。
        # figsize=(12, 8): 設定圖形的尺寸。figsize 是一個元組，表示圖形的寬度和高度，單位是英寸（inches）。
        # dpi=200: 設定圖形的解析度。dpi 代表 "dots per inch"（每英寸點數），它決定了圖形的解析度。在這個例子中，dpi=200 表示每英寸有 200 個點，這將使圖形的細節更為清晰。高 dpi 值通常用於生成高質量的圖像文件。
        
        table = plt.table(cellText = result.values,  # cellText：表格中的數據
                          rowLabels = result.index,  # rowLabels：表格的行標籤
                          colLabels = result.columns,  # colLabels：表格的列標籤
                          cellLoc = 'center',  # cellLoc：表格單元格中文字的位置
                          loc = 'center')  # loc：表格在圖中的位置
        
        # 設置表格樣式
        table.auto_set_font_size(True)  # 自動調整字體大小
        table.set_fontsize(10)  # 設置字體大小
        table.scale(1, 1)  # 調整表格的縮放比例
        
        # 繪製格線（使用 table 的內建方法）
        for key, cell in table.get_celld().items():  # 遍歷表格中的所有單元格，返回的 key 是單元格的行列索引，cell 是單元格對象
            if key[0] in result.index and key[1] in result.columns:  # 檢查單元格的行和列是否在結果的索引和列中
                cell.set_edgecolor('black')  # 設置單元格邊框顏色為黑色
                cell.set_linewidth(0.05)  # 設置單元格邊框的線寬
        
        # 隱藏坐標軸
        plt.axis('off')

    def _plot_a_line(self, data, title):
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
        # 顯示網格線
        plt.grid(True)

    def _plot_two_line(self, data, title):
        # 繪製雙折線圖
        plt.figure(figsize=(10, 6))
        # 繪製 "TV Show" 的年份數據，設定顏色
        plt.plot(self.tv_show_year_counts.index, self.tv_show_year_counts.values, label='TV Show', color='#E50611')
        # 繪製 "Movie" 的年份數據，設定顏色
        plt.plot(self.movie_year_counts.index, self.movie_year_counts.values, label='Movie', color='#000000')
        # 添加圖表標題和軸標籤
        plt.title(title)
        plt.xlabel('Year')
        plt.ylabel('Count')
        # 確保這裡的index是每一年的列表
        plt.xticks(self.tv_show_year_counts.index)
        # 顯示圖例
        plt.legend()
        # 顯示網格線
        plt.grid(True)
  
    def _plot_combine_b2l(self, data, title):
        
        # 確保所有年份都在同一範圍內
        years = sorted(set(self.tv_show_year_counts.index).union(self.movie_year_counts.index))
        
        # 將缺失的年份填充為 0
        self.tv_show_year_counts = self.tv_show_year_counts.reindex(years, fill_value=0)
        self.movie_year_counts = self.movie_year_counts.reindex(years, fill_value=0)
        
        # 計算總和年增長量
        self.total_year_counts = self.tv_show_year_counts + self.movie_year_counts
        
        # 創建圖表和第一個子圖（長條圖）
        fig, ax1 = plt.subplots(figsize=(12, 8))
        
        # 繪製長條圖，顯示 TV Shows 和 Movies 的總和年增長量
        ax1.bar(years, self.total_year_counts, color='tab:blue', alpha=0.6, label='Total Contents')
        
        # 設置第一個子圖的標題和 X 軸標籤
        ax1.set_title('Yearly Growth of TV Shows and Movies on Netflix')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Total Number of Contents', color='tab:blue')
        
        # 設置 Y 軸的刻度顏色
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        
        # 創建第二個共享 X 軸的子圖
        ax2 = ax1.twinx()
        ax2.set_ylabel('Number of Contents', color='black')
        
        # 設置相同的 Y 軸範圍
        ax1_ylim = ax1.get_ylim()
        ax2.set_ylim(ax1_ylim)
        
        # 繪製雙折線圖
        ax2.plot(years, self.tv_show_year_counts, label='TV Shows', color='#E50611', marker='o', alpha=0.75)
        ax2.plot(years, self.movie_year_counts, label='Movies', color='black', marker='o', alpha=1)
        
        # 設置第二個 Y 軸的顏色
        ax2.tick_params(axis='y', labelcolor='black')
        
        # 添加圖例
        ax2.legend(loc='upper left')



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

    # 生成並保存柱狀圖
    analysis.visualize('bar', 'type')
    analysis.export('content type bar.png')

    # 生成並保存圓餅圖
    analysis.visualize('pie', 'rating')
    analysis.export('content rating pie.png')

    # 生成並保存熱力圖
    analysis.visualize('heatmap', 'date_added')
    analysis.export('content addition heatmap.png')

    # 生成並保存統計表
    analysis.visualize('table', 'date_added')
    analysis.export('content addition table.png')
    
    # 生成並保存單折線圖
    analysis.visualize('a_line', 'year')
    analysis.export('yearly content addition line.png')
    
    # 生成並保存雙折線圖
    analysis.visualize('two_line', 'year')
    analysis.export('Yearly Counts of TV Shows and Movies.png')

    # 生成並保存組合圖
    analysis.visualize('combine_b2l', 'year')
    analysis.export('Yearly Growth of TV Shows and Movies on Netflix.png')



def main():
    mySQLConnector()
    analysis()

if __name__ == "__main__":
    main()


