import mysql.connector
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

from dotenv import load_dotenv
from utils.data_utils_mysql import MySQLConnector
from utils.data_utils_mysql import Analysis

# 載入 .env 檔案中的環境變數
load_dotenv()

def main():
    # print('test')
    # 創建 Analysis 實例，指定資料表名稱
    analysis = Analysis('data_netflix')
    # 從數據庫獲取數據
    analysis.get_data()
    # 進行數據計算
    analysis.calculate()


    # # 分析影片類型（'type'列），並產生圖表

    # # 生成柱狀圖
    # analysis.visualize('bar', 'type')
    # analysis.export('content_type_bar.png')

    # # 生成圓餅圖
    # analysis.visualize('pie', 'type')
    # analysis.export('content_type_pie.png')


    # 分析上架日期（'date_add'列），並產生圖表
    
    # # 生成統計表格
    # analysis.visualize('table', 'date_added')
    # analysis.export('yearly_content_addition.png')

    # 生成熱力圖
    analysis.visualize('heatmap', 'month_year')
    analysis.export('content_addition_heatmap.png')    
    


if __name__ == "__main__":
    main()
