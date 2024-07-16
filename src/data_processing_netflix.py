import pandas as pd
import os
from utils.data_utils import preprocess_data, save_data



# 定義數據文件路徑
# 透過 os.path.join() 函式將導入文件路徑，這個方法具有話平台的兼容性

# 原始數據
raw_data_path = os.path.join('data', 'raw', 'netflix_titles.csv')
# 整理過後
processed_data_path = os.path.join('data', 'processed', 'netflix_titles_cleaned.csv')



# 收集數據

def collect_data(path):  # 定義了一個名為 collect_data 的函數
    df = pd.read_csv(path)  # 使用 Pandas 的 read_csv 函數從指定路徑讀取 CSV 檔，並將其內容存儲在變數 df 中
    return df  # 返回 df 變數，從 CSV 檔中讀取的資料框

