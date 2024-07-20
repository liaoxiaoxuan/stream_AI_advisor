import pandas as pd  # 用於數據處理和分析。
import os
import seaborn as sns  # seaborn 提供高級抽象層，讓複雜的圖表生成變得簡單且美觀。
import matplotlib.pyplot as plt  # matplotlib 提供底層功能，讓用戶可以對圖表進行詳細的控制和定制。



# 定義（整理後的）數據文件路徑

processed_data_path = os.path.join('data', 'processed', 'netflix_titles_processed.csv')



if __name__ == "__main__":
    print("Loading raw Netflix data...")  # 輸出通知：即將載入原始的 Netflix 資料
    df_netflix_cleaned = pd.read_csv(processed_data_path)  # 使用 pandas 的 read_csv 函數讀取 CSV 文件並將其存儲在 df_netflix_cleaned 數據框中。

    # 輸出載入的數據
    print("Netflix data loaded successfully:")

    # 定義要寫入的內容
    content = (
        f"Netflix data loaded successfully:\n"
        f"前幾行：\n{df_netflix_cleaned.head()}\n"
        "-----------------------------------------------------\n"
        f"列數和欄數：\n{df_netflix_cleaned.shape}\n"
        "-----------------------------------------------------\n"
        f"總數據量：\n{df_netflix_cleaned.size}\n"
        "-----------------------------------------------------\n"
        f"所有欄位名稱：\n{df_netflix_cleaned.columns}\n"
        "-----------------------------------------------------\n"
        f"摘要資訊：\n"
    )

    # 將 info 輸出重定向到 content 中
    # 將 info() 的完整輸出（包括所有細節）添加到 content 中，以確保 info() 的所有信息都被完整地寫入到文件中。

    from io import StringIO  # 從 io 模組中導入 StringIO 類，用於創建內存中的字符串緩衝區
    buffer = StringIO()  # 創建一個 StringIO 實例，作為內存中的緩衝區
    df_netflix_cleaned.info(buf=buffer)  # 將 DataFrame 的 info 輸出重定向到緩衝區中
    info_str = buffer.getvalue()  # 從緩衝區中獲取內容，並將其存儲為字符串
    content += info_str + "-----------------------------------------------------\n"  # 將 info 字符串和分隔線添加到 content 中
    
    content += (
        f"記憶體使用量：\n{df_netflix_cleaned.memory_usage()}\n"
        "-----------------------------------------------------\n"
        f"重複行的數量：\n{df_netflix_cleaned.duplicated().sum()}\n"
        "-----------------------------------------------------\n"
        f"每個欄位的缺失值數量：\n{df_netflix_cleaned.isna().sum()}\n"
        "-----------------------------------------------------\n"
        f"所有欄位的數據類型：\n{df_netflix_cleaned.dtypes.unique()}\n"
        "-----------------------------------------------------\n"
    )
    
# # 寫入到txt文件中
# output_file = os.path.join('reports', 'collect_data', 'N_data_cleaned_summary.txt')
# os.makedirs(os.path.dirname(output_file), exist_ok=True)  # 建立目標文件路徑中的所有目錄，並確保如果目錄已經存在，不會引發錯誤。
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(content)

# print(f"資料摘要已成功寫入到 {output_file} 文件中。")



# 加載數據集
netflix_overall = pd.read_csv(processed_data_path)

# # 顯示數據集的前五行
# print(netflix_overall.head())



# 分析影片類型（'type'列），並產生圖表


# # 篩選出 'type' 列值為 'TV Show' 和 'Movie' 的數據
# netflix_shows = netflix_overall[netflix_overall['type'] == 'TV Show']  # 篩選出 'type' 列值為 'TV Show' 的數據，並存儲在 netflix_shows 變量中
# netflix_movies = netflix_overall[netflix_overall['type'] == 'Movie']   # 篩選出 'type' 列值為 'Movie' 的數據，並存儲在 netflix_movies 變量中

# 計算並輸出電影和電視節目的數量
num_movies = netflix_overall[netflix_overall['type'] == 'Movie'].shape[0]  # 計算 'type' 列為 'Movie' 的行數
num_shows = netflix_overall[netflix_overall['type'] == 'TV Show'].shape[0]  # 計算 'type' 列為 'TV Show' 的行數

print(f"Number of Movies: {num_movies}")  # 輸出電影的數量
print(f"Number of TV Shows: {num_shows}")  # 輸出電視節目的數量





