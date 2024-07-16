import pandas as pd
import os
from utils.data_utils import preprocess_data, save_data



# 定義數據文件路徑
# 透過 os.path.join() 函式將導入文件路徑，這個方法具有話平台的兼容性

# 原始數據
raw_data_path = os.path.join('data', 'raw', 'netflix_titles.csv')
# 整理過後
processed_data_path = os.path.join('data', 'processed', 'netflix_titles_cleaned.csv')



# 定義收集數據的函數

def collect_data(path):  # 定義了一個名為 collect_data 的函數
    df = pd.read_csv(path)  # 使用 Pandas 的 read_csv 函數從指定路徑讀取 CSV 檔，並將其內容存儲在變數 df 中
    return df  # 返回 df 變數，從 CSV 檔中讀取的資料框



# 主程式執行時收集數據

if __name__ == "__main__":
    print("Loading raw Netflix data...")  # 輸出通知：即將載入原始的 Netflix 資料
    df_netflix = collect_data(raw_data_path)  # 調用 collect_data 函數，從 raw_data_path 指定的路徑載入原始的 Netflix 資料，並將結果存儲在變數 df_netflix 中

    # 輸出載入的數據
    print("Netflix data loaded successfully:")
    print(f"前幾行：\n{df_netflix.head()}")                     # 前幾行
    print("-----------------------------------------------------")
    print(f"列數和欄數：\n{df_netflix.shape}")                   # 列數和欄數
    print("-----------------------------------------------------")
    print(f"總數據量：\n{df_netflix.size}")                      # 總數據量
    print("-----------------------------------------------------")
    print(f"所有欄位名稱：\n{df_netflix.columns}")               # 所有欄位名稱
    print("-----------------------------------------------------")
    print(f"摘要資訊：\n{df_netflix.info()}")                    # 摘要資訊（包括每個欄位的非空值數量和數據類型）
    print("-----------------------------------------------------")
    print(f"記憶體使用量：\n{df_netflix.memory_usage()}")         # 記憶體使用量
    print("-----------------------------------------------------")
    print(f"重複行的數量：\n{df_netflix.duplicated().sum()}")     # 重複行的數量
    print("-----------------------------------------------------")
    print(f"每個欄位的缺失值數量：\n{df_netflix.isna().sum()}")    # 每個欄位的缺失值數量
    print("-----------------------------------------------------")
    print(f"所有欄位的數據類型：\n{df_netflix.dtypes.unique()}")   # 所有欄位的數據類型
    print("-----------------------------------------------------")

    # # 預處理數據
    # print("Preprocessing Netflix data...")   # 輸出通知：即將預處理原始的 Netflix 資料
    # df_netflix_cleaned = preprocess_data(df_netflix)  # 調用 preprocess_data 函數，對 df_netflix 中的資料進行預處理，並將結果存儲在變數 df_netflix_cleaned 中