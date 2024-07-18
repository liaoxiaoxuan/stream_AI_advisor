import pandas as pd
import os
from utils.data_utils import preprocess_data, save_data



# 定義數據文件路徑
# 透過 os.path.join() 函式將導入文件路徑，這個方法具有話平台的兼容性

# 原始數據
raw_data_path = os.path.join('data', 'raw', 'disney_plus_titles.csv')
# 整理過後
processed_data_path = os.path.join('data', 'processed', 'disney_plus_titles_processed.csv')



# 定義收集數據的函數

def collect_data(path):  # 定義了一個名為 collect_data 的函數
    df = pd.read_csv(path)  # 使用 Pandas 的 read_csv 函數從指定路徑讀取 CSV 檔，並將其內容存儲在變數 df 中
    return df  # 返回 df 變數，從 CSV 檔中讀取的資料框



# 主程式執行時收集數據

if __name__ == "__main__":
    print("Loading raw disney_plus data...")  # 輸出通知：即將載入原始的 Disney+ 資料
    df_disney_plus = collect_data(raw_data_path)  # 調用 collect_data 函數，從 raw_data_path 指定的路徑載入原始的 Disney+ 資料，並將結果存儲在變數 df_netflix 中

    # # 輸出載入的數據
    # print("disney_plus data loaded successfully:")
    # # 定義要寫入的內容
    # content = (
    #     f"disney_plus data loaded successfully:\n"
    #     f"前幾行：\n{df_disney_plus.head()}\n"
    #     "-----------------------------------------------------\n"
    #     f"列數和欄數：\n{df_disney_plus.shape}\n"
    #     "-----------------------------------------------------\n"
    #     f"總數據量：\n{df_disney_plus.size}\n"
    #     "-----------------------------------------------------\n"
    #     f"所有欄位名稱：\n{df_disney_plus.columns}\n"
    #     "-----------------------------------------------------\n"
    #     f"摘要資訊：\n{df_disney_plus.info()}\n"
    #     "-----------------------------------------------------\n"
    #     f"記憶體使用量：\n{df_disney_plus.memory_usage()}\n"
    #     "-----------------------------------------------------\n"
    #     f"重複行的數量：\n{df_disney_plus.duplicated().sum()}\n"
    #     "-----------------------------------------------------\n"
    #     f"每個欄位的缺失值數量：\n{df_disney_plus.isna().sum()}\n"
    #     "-----------------------------------------------------\n"
    #     f"所有欄位的數據類型：\n{df_disney_plus.dtypes.unique()}\n"
    #     "-----------------------------------------------------\n"
    # )
    
    # # 寫入到txt文件中
    # output_file = os.path.join('reports', 'collect_data', 'D_data_summary.txt')
    # with open(output_file, "w", encoding="utf-8") as file:
    #     file.write(content)
    
    # print(f"資料摘要已成功寫入到 {output_file} 文件中。")


    # 預處理數據
    print("Preprocessing Disney+ data...")   # 輸出通知：即將預處理原始的 Disney+ 資料
    df_disney_plus_cleaned = preprocess_data(df_disney_plus)  # 調用 preprocess_data 函數，對 df_netflix 中的資料進行預處理，並將結果存儲在變數 df_netflix_cleaned 中

    # 輸出整理結果至 terminal
    print(f"Preprocessing Disney+ data（first 20 rows）：\n{df_disney_plus_cleaned.head(20)}\n")


    # 儲存處理後的數據
    save_data(df_disney_plus_cleaned, processed_data_path)  # 調用 save_data 函數，將預處理後的資料保存到 processed_data_path 指定的路徑
    print(f"Processed data saved to {processed_data_path}")  # 輸出通知：預處理後的資料已成功保存到指定路徑
    