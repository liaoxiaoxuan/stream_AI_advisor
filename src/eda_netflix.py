import pandas as pd  # 用於數據處理和分析。
import os
import seaborn as sns  # seaborn 提供高級抽象層，讓複雜的圖表生成變得簡單且美觀。
import matplotlib.pyplot as plt  # matplotlib 提供底層功能，讓用戶可以對圖表進行詳細的控制和定制。
import numpy as np  # 數值計算庫，，主要用於處理大型多維陣列和矩陣運算，以及提供大量的數學函數庫來操作這些陣列。



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



# # 分析影片類型（'type'列），並產生圖表


# # # 篩選出 'type' 列值為 'TV Show' 和 'Movie' 的數據
# # netflix_shows = netflix_overall[netflix_overall['type'] == 'TV Show']  # 篩選出 'type' 列值為 'TV Show' 的數據，並存儲在 netflix_shows 變量中
# # netflix_movies = netflix_overall[netflix_overall['type'] == 'Movie']   # 篩選出 'type' 列值為 'Movie' 的數據，並存儲在 netflix_movies 變量中


# # 計算並輸出電影和電視節目的數量
# num_movies = netflix_overall[netflix_overall['type'] == 'Movie'].shape[0]  # 計算 'type' 列為 'Movie' 的行數
# num_shows = netflix_overall[netflix_overall['type'] == 'TV Show'].shape[0]  # 計算 'type' 列為 'TV Show' 的行數
# print(f"Number of Movies: {num_movies}")  # 輸出電影的數量
# print(f"Number of TV Shows: {num_shows}")  # 輸出電視節目的數量


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


# # 繪製圓餅圖

# labels = ['Movies', 'TV Shows']  # 圓餅圖的標籤
# sizes = [num_movies, num_shows]  # 每塊圓餅的大小對應電影和電視節目的數量
# colors = ['#ff9999', '#66b3ff']  # 每塊圓餅的顏色，電影用紅色，電視節目用藍色
# explode = (0.1, 0)  # 將第一塊（電影）突出顯示，突出顯示的比例為 0.1

# fig1, ax1 = plt.subplots()  # 創建一個新的圖和子圖
# ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        # shadow=True, startangle=90)  # 繪製圓餅圖
# # sizes: 圓餅每塊的大小
# # explode: 突出顯示的比例
# # labels: 標籤
# # colors: 顏色
# # autopct: 顯示百分比，格式為 1.1%
# # shadow: 添加陰影
# # startangle: 起始角度，設定為 90 度，使第一塊從 90 度開始繪製

# ax1.axis('equal')  # 確保圓餅圖是圓形
# plt.title("Proportion of Movies vs TV Shows on Netflix")  # 設置圖表標題

# # 保存圓餅圖
# plot_file_pie = os.path.join('reports', 'collect_data', 'N_pie_chart.png')  # 圓餅圖的儲存路徑
# os.makedirs(os.path.dirname(plot_file_pie), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# plt.savefig(plot_file_pie)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用
# print(f"圓餅圖已保存到 {plot_file_pie} 文件中。")  # 輸出一條消息到終端，告知用戶圖表已成功保存到指定的文件路徑



# # 分析上架日期（'date_add'列），並產生圖表（影片更新頻率熱力圖）


# # 確保 'date_added' 列是日期時間格式
# netflix_overall['date_added'] = pd.to_datetime(netflix_overall['date_added'], format='%Y/%m/%d')
# # pd.to_datetime 用來將 date_added 列轉換為 datetime 類型
# # print(netflix_overall['date_added'])

# # 提取年份和月份
# netflix_date = netflix_overall[['date_added']].dropna()  # 從 netflix_overall 中提取 'date_added' 列，並刪除空值
# netflix_date['year'] = netflix_date['date_added'].dt.year  # 提取年份
# netflix_date['month'] = netflix_date['date_added'].dt.month_name()  # 提取月份名稱
# # 檢查創建的列
# # print(netflix_date.head())
# # print(netflix_date.columns)
# # 計算每個年份中各個月份的頻次
# month_counts = netflix_date.groupby('year')['month'].value_counts()  # month_counts 將會是一個 Series，其中包含每個年份和月份的計數，索引是 MultiIndex，第一層是年份，第二層是月份。
# # print(month_counts)

# # 定義月份順序，並反轉順序
# month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  #[::-1]
# # print(month_order)

# # 排列為矩陣
# matrix = month_counts.unstack()  # 先使用 unstack() 將月份從行索引轉為列索引，未出現的月份會變成 NaN
# matrix = matrix.fillna(0)  # 使用 fillna(0) 將 NaN 值填充為 0
# matrix = matrix.astype(int)  # 將數據類型轉換為整數
# matrix = matrix[month_order]  # 根據指定的月份順序重新排序列
# result = matrix.T  # 將矩陣轉置，讓年份成為列索引，月份成為行索引
# # print(result)


# # # 計算年和月的總和

# # result['Month Total'] = result.sum(axis=1)  # 計算每年的總和，並將結果新增至 DataFrame 的新列 'Year Total'
# # result.loc['Year Total'] = result.sum(axis=0)  # 計算每月的總和，並將結果新增至 DataFrame 的新行 'Month Total'


# # # 繪製表格

# # # 設置圖表大小和分辨率
# # plt.figure(figsize=(12, 8), dpi=300)
# # # plt.figure(): 創建一個新的圖形對象，這是 Matplotlib 用來顯示和處理圖形的容器。
# # # figsize=(12, 8): 設定圖形的尺寸。figsize 是一個元組，表示圖形的寬度和高度，單位是英寸（inches）。
# # # dpi=200: 設定圖形的解析度。dpi 代表 "dots per inch"（每英寸點數），它決定了圖形的解析度。在這個例子中，dpi=200 表示每英寸有 200 個點，這將使圖形的細節更為清晰。高 dpi 值通常用於生成高質量的圖像文件。

# # table = plt.table(cellText=result.values,  # cellText：表格中的數據
                # #   rowLabels=result.index,  # rowLabels：表格的行標籤
                # #   colLabels=result.columns,  # colLabels：表格的列標籤
                # #   cellLoc='center',  # cellLoc：表格單元格中文字的位置
                # #   loc='center')  # loc：表格在圖中的位置

# # # 設置表格樣式
# # table.auto_set_font_size(True)  # 自動調整字體大小
# # table.set_fontsize(10)  # 設置字體大小
# # table.scale(1, 1)  # 調整表格的縮放比例

# # # 繪製格線（使用 table 的內建方法）
# # for key, cell in table.get_celld().items():  # 遍歷表格中的所有單元格，返回的 key 是單元格的行列索引，cell 是單元格對象
    # # if key[0] in result.index and key[1] in result.columns:  # 檢查單元格的行和列是否在結果的索引和列中
        # # cell.set_edgecolor('black')  # 設置單元格邊框顏色為黑色
        # # cell.set_linewidth(0.05)  # 設置單元格邊框的線寬

# # # 隱藏坐標軸
# # plt.axis('off')

# # # 保存表格為圖片
# # plt_file_count_table = os.path.join('reports', 'collect_data', 'N_date_add_count_table.png')  # 表格的儲存路徑
# # os.makedirs(os.path.dirname(plt_file_count_table), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# # plt.savefig(plt_file_count_table, bbox_inches='tight')  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# # plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用


# # 繪製熱力圖
# plt.figure(figsize=(10, 7), dpi=200)  # 設置圖表大小和分辨率
# plt.pcolor(result, cmap='afmhot_r', edgecolors='white', linewidths=2)  # 使用顏色地圖繪製熱力圖
# plt.xticks(np.arange(0.5, len(result.columns), 1), result.columns, fontsize=7, fontfamily='serif')  # 設置 x 軸標籤
# plt.yticks(np.arange(0.5, len(result.index), 1), result.index, fontsize=7, fontfamily='serif')  # 設置 y 軸標籤
# plt.title('Netflix Contents Update', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))  # 設置圖表標題
# cbar = plt.colorbar()  # 顯示顏色條
# cbar.ax.tick_params(labelsize=8)  # 設置顏色條標籤大小
# cbar.ax.minorticks_on()  # 啟用顏色條的小刻度

# # # 在熱力圖的每個單元格上顯示數值
# # for i in range(len(result.index)):  # 遍歷行索引
# #     for j in range(len(result.columns)):  # 遍歷列索引
# #         plt.text(j + 0.5, i + 0.5, int(result.iloc[i, j]),  # 在 (j + 0.5, i + 0.5) 位置添加文本，文本內容為對應單元格的整數值
# #                  ha='center', va='center',  # 設置文本的水平和垂直對齊方式為居中
# #                  fontsize=8, color='black')  # 設置文本的字體大小為 8，顏色為黑色

# # 保存熱力圖為圖片
# plt_file_count_heatmap = os.path.join('reports', 'figures', 'N_date_add_heatmap.png')  # 表格的儲存路徑
# os.makedirs(os.path.dirname(plt_file_count_heatmap), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# plt.savefig(plt_file_count_heatmap)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用



# 分析發行年分（'release_year'列），並產生圖表


# 繪製長條圖
plt.figure(figsize=(12,10)) # 設置圖表大小
sns.set(style="darkgrid") # 設置 Seaborn 的樣式為 "darkgrid"
ax = sns.countplot(y="release_year", data=netflix_overall, palette="Set2", order=netflix_overall['release_year'].value_counts().index[0:15]) # 使用 Seaborn 繪製柱狀圖，顯示每年發布的電影數量，並按年份排序
ax.set_title("Number of Movies Released by Netflix Each Year", fontsize=16)  # 設置圖表標題

# 將統計數字顯示在長條圖上
for container in ax.containers:  # 使用迴圈來依次訪問每根長條
    ax.bar_label(container, fmt='%d', label_type='edge', padding=3)  # 在當前條形容器上添加數字標籤
    # fmt='%d': 指定標籤的格式為整數
    # label_type='edge': 將標籤顯示在長條的邊緣
    # padding=3: 設定標籤與條形之間的間距為3個像素


# 保存圖片
plot_file = os.path.join('reports', 'collect_data', 'N_release_year_bar.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑
os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑

plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用



# 分析年齡分級（'rating'列），並產生圖表
# 分析影片時長（'duration'列），並產生圖表