import pandas as pd
import os



# 定義（整理後的）數據文件路徑

processed_data_path = os.path.join('data', 'processed', 'disney_plus_titles_processed.csv')



if __name__ == "__main__":
    print("Loading raw disney_plus data...")  # 輸出通知：即將載入原始的 Disney+ 資料
    df_disney_plus_cleaned = pd.read_csv(processed_data_path)  # 使用 pandas 的 read_csv 函數讀取 CSV 文件並將其存儲在 df_disney_plus_cleaned 數據框中。

    # 輸出載入的數據
    print("disney_plus data loaded successfully:")
    # 定義要寫入的內容
    content = (
        f"disney_plus data loaded successfully:\n"
        f"前幾行：\n{df_disney_plus_cleaned.head()}\n"
        "-----------------------------------------------------\n"
        f"列數和欄數：\n{df_disney_plus_cleaned.shape}\n"
        "-----------------------------------------------------\n"
        f"總數據量：\n{df_disney_plus_cleaned.size}\n"
        "-----------------------------------------------------\n"
        f"所有欄位名稱：\n{df_disney_plus_cleaned.columns}\n"
        "-----------------------------------------------------\n"
        f"摘要資訊：\n{df_disney_plus_cleaned.info()}\n"
        "-----------------------------------------------------\n"
        f"記憶體使用量：\n{df_disney_plus_cleaned.memory_usage()}\n"
        "-----------------------------------------------------\n"
        f"重複行的數量：\n{df_disney_plus_cleaned.duplicated().sum()}\n"
        "-----------------------------------------------------\n"
        f"每個欄位的缺失值數量：\n{df_disney_plus_cleaned.isna().sum()}\n"
        "-----------------------------------------------------\n"
        f"所有欄位的數據類型：\n{df_disney_plus_cleaned.dtypes.unique()}\n"
        "-----------------------------------------------------\n"
    )
    
    # 寫入到txt文件中
    output_file = os.path.join('reports', 'collect_data', 'D_data_cleaned_summary.txt')
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"資料摘要已成功寫入到 {output_file} 文件中。")