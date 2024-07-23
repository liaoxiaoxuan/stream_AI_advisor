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


# # 繪製長條圖

# # 分析電影與電視節目的數量對比
# sns.set(style="darkgrid")  # 設定 Seaborn 的繪圖樣式為 "darkgrid"，這會影響圖表的背景網格樣式，使其更適合呈現統計數據
# ax = sns.countplot(x="type", data=netflix_overall, palette="Set2")  # 使用 Seaborn 的 countplot 函數繪製柱狀圖，x 軸為 "type" 欄位，數據來源為 netflix_overall，使用 "Set2" 調色盤
# plt.title("Comparison of Movie vs TV Show on Netflix")  # 設置圖表標題
# plt.xlabel("Type")  # 設置 x 軸標籤
# plt.ylabel("Count")  # 設置 y 軸標籤

# # 在長條圖上顯示統計數字
# for p in ax.patches:  # 遍歷每個柱狀圖的 patch（即每個柱子）
    # height = p.get_height()  # 獲取柱子的高度，即統計數字
    # ax.text(p.get_x() + p.get_width() / 2., height + 10,  # 在柱子上方添加文本標籤，位置略高於柱子的頂端
            # f'{int(height)}',  # 顯示的數字，轉換為整數
            # ha='center',  # 水平對齊方式為中心
            # va='bottom')  # 垂直對齊方式為底部

# # 保存圖片
# plot_file = os.path.join('reports', 'collect_data', 'N_type.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑，包含目錄路徑 'reports/collect_data' 和文件名 'N_type.png'
# os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑

# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用
# print(f"分析圖已保存到 {plot_file} 文件中。")  # 輸出一條消息到終端，告知用戶圖表已成功保存到指定的文件路徑


# 繪製圓餅圖

labels = ['Movies', 'TV Shows']  # 圓餅圖的標籤
sizes = [num_movies, num_shows]  # 每塊圓餅的大小對應電影和電視節目的數量
colors = ['#ff9999', '#66b3ff']  # 每塊圓餅的顏色，電影用紅色，電視節目用藍色
explode = (0.1, 0)  # 將第一塊（電影）突出顯示，突出顯示的比例為 0.1

fig1, ax1 = plt.subplots()  # 創建一個新的圖和子圖
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)  # 繪製圓餅圖
# sizes: 圓餅每塊的大小
# explode: 突出顯示的比例
# labels: 標籤
# colors: 顏色
# autopct: 顯示百分比，格式為 1.1%
# shadow: 添加陰影
# startangle: 起始角度，設定為 90 度，使第一塊從 90 度開始繪製

ax1.axis('equal')  # 確保圓餅圖是圓形
plt.title("Proportion of Movies vs TV Shows on Netflix")  # 設置圖表標題

# 保存圓餅圖
plot_file_pie = os.path.join('reports', 'collect_data', 'N_pie_chart.png')  # 圓餅圖的儲存路徑
os.makedirs(os.path.dirname(plot_file_pie), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
plt.savefig(plot_file_pie)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用
print(f"圓餅圖已保存到 {plot_file_pie} 文件中。")  # 輸出一條消息到終端，告知用戶圖表已成功保存到指定的文件路徑

