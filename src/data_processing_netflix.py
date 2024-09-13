import pandas as pd
import os
from datetime import datetime
from utils.data_utils import preprocess_data, save_data



# 定義數據文件路徑
# 透過 os.path.join() 函式將導入文件路徑，這個方法具有話平台的兼容性

# 原始數據
raw_data_path = os.path.join('D:/PYTHON/oo_hank_project/stream_AI_advisor/data/raw/netflix_titles.csv')
# 整理過後
processed_data_path = os.path.join('D:/PYTHON/oo_hank_project/stream_AI_advisor/data/processed/netflix_titles_processed.csv')



# 定義收集數據的函數

def collect_data(path):  # 定義了一個名為 collect_data 的函數
    df = pd.read_csv(path)  # 使用 Pandas 的 read_csv 函數從指定路徑讀取 CSV 檔，並將其內容存儲在變數 df 中
    return df  # 返回 df 變數，從 CSV 檔中讀取的資料框



# 定義日期轉換函數
def convert_date_format(date_str):
    if isinstance(date_str, str):  # 確保 date_str 是字符串
        try:
            # 解析原始日期字符串
            date_obj = datetime.strptime(date_str, '%B %d, %Y')
            # 轉換為 MySQL 所需的日期格式
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            # 處理格式不正確的日期
            return None
    else:
        # 處理非字符串類型
        return None



# 主程式執行時收集數據

if __name__ == "__main__":
    print("Loading raw Netflix data...")  # 輸出通知：即將載入原始的 Netflix 資料
    df_netflix = collect_data(raw_data_path)  # 調用 collect_data 函數，從 raw_data_path 指定的路徑載入原始的 Netflix 資料，並將結果存儲在變數 df_netflix 中

    # # 輸出載入的數據
    # print("Netflix data loaded successfully:")
    # # 定義要寫入的內容
    # content = (
        # f"Netflix data loaded successfully:\n"
        # f"前幾行：\n{df_netflix.head()}\n"
        # "-----------------------------------------------------\n"
        # f"列數和欄數：\n{df_netflix.shape}\n"
        # "-----------------------------------------------------\n"
        # f"總數據量：\n{df_netflix.size}\n"
        # "-----------------------------------------------------\n"
        # f"所有欄位名稱：\n{df_netflix.columns}\n"
        # "-----------------------------------------------------\n"
        # f"摘要資訊：\n{df_netflix.info()}\n"
        # "-----------------------------------------------------\n"
        # f"記憶體使用量：\n{df_netflix.memory_usage()}\n"
        # "-----------------------------------------------------\n"
        # f"重複行的數量：\n{df_netflix.duplicated().sum()}\n"
        # "-----------------------------------------------------\n"
        # f"每個欄位的缺失值數量：\n{df_netflix.isna().sum()}\n"
        # "-----------------------------------------------------\n"
        # f"所有欄位的數據類型：\n{df_netflix.dtypes.unique()}\n"
        # "-----------------------------------------------------\n"
    # )
    
    # # 寫入到txt文件中
    # output_file = os.path.join('reports', 'collect_data', 'N_data_summary.txt')
    # with open(output_file, "w", encoding="utf-8") as file:
        # file.write(content)
    
    # print(f"資料摘要已成功寫入到 {output_file} 文件中。")


    # 日期格式轉換
    if 'date_added' in df_netflix.columns:
        df_netflix['date_added'] = df_netflix['date_added'].apply(convert_date_format)


    # 預處理數據
    print("Preprocessing Netflix data...")   # 輸出通知：即將預處理原始的 Netflix 資料
    df_netflix_cleaned = preprocess_data(df_netflix)  # 調用 preprocess_data 函數，對 df_netflix 中的資料進行預處理，並將結果存儲在變數 df_netflix_cleaned 中

    from datetime import datetime



    # 輸出整理結果至 terminal
    print(f"Preprocessing Netflix data（first 20 rows）：\n{df_netflix_cleaned.head(20)}\n")


    # 儲存處理後的數據
    save_data(df_netflix_cleaned, processed_data_path)  # 調用 save_data 函數，將預處理後的資料保存到 processed_data_path 指定的路徑
    print(f"Processed data saved to {processed_data_path}")  # 輸出通知：預處理後的資料已成功保存到指定路徑
    