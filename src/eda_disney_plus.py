import pandas as pd  # 用於數據處理和分析。
import os
import seaborn as sns  # seaborn 提供高級抽象層，讓複雜的圖表生成變得簡單且美觀。
import matplotlib.pyplot as plt  # matplotlib 提供底層功能，讓用戶可以對圖表進行詳細的控制和定制。
import numpy as np  # 數值計算庫，，主要用於處理大型多維陣列和矩陣運算，以及提供大量的數學函數庫來操作這些陣列。
import plotly.graph_objects as go  # 使用 Plotly 的功能來創建和顯示交互式圖表和圖形



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
        f"摘要資訊：\n"
    )

    # 將 info 輸出重定向到 content 中
    # 將 info() 的完整輸出（包括所有細節）添加到 content 中，以確保 info() 的所有信息都被完整地寫入到文件中。
    
    from io import StringIO  # 從 io 模組中導入 StringIO 類，用於創建內存中的字符串緩衝區
    buffer = StringIO()  # 創建一個 StringIO 實例，作為內存中的緩衝區
    df_disney_plus_cleaned.info(buf=buffer)  # 將 DataFrame 的 info 輸出重定向到緩衝區中
    info_str = buffer.getvalue()  # 從緩衝區中獲取內容，並將其存儲為字符串
    content += info_str + "-----------------------------------------------------\n"  # 將 info 字符串和分隔線添加到 content 中
    
    content += (    
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
    
    # # 寫入到txt文件中
    # output_file = os.path.join('reports', 'collect_data', 'D_data_cleaned_summary.txt')
    # os.makedirs(os.path.dirname(output_file), exist_ok=True)  # 建立目標文件路徑中的所有目錄，並確保如果目錄已經存在，不會引發錯誤。
    # with open(output_file, "w", encoding="utf-8") as file:
        # file.write(content)
    
    # print(f"資料摘要已成功寫入到 {output_file} 文件中。")



# 加載數據集
disney_plus_overall = pd.read_csv(processed_data_path)

# # 顯示數據集的前五行
# print(disney_plus_overall.head())

# 分割數據集
d1 = disney_plus_overall[disney_plus_overall["type"] == "TV Show"]  # 篩選出 "type" 列為 "TV Show" 的資料過濾出來並賦值給 d1
d2 = disney_plus_overall[disney_plus_overall["type"] == "Movie"]  # 篩選出 "type" 列為 "Movie" 的資料過濾出來並賦值給 d2
# print(d1)
# print(d2)


# # 分析影片類型（'type'列），並產生圖表


# # # 篩選出 'type' 列值為 'TV Show' 和 'Movie' 的數據
# # disney_plus_shows = disney_plus_overall[disney_plus_overall['type'] == 'TV Show']  # 篩選出 'type' 列值為 'TV Show' 的數據，並存儲在 disney_plus_shows 變量中
# # disney_plus_movies = disney_plus_overall[disney_plus_overall['type'] == 'Movie']   # 篩選出 'type' 列值為 'Movie' 的數據，並存儲在 disney_plus_movies 變量中


# # 計算並輸出電影和電視節目的數量
# num_movies = disney_plus_overall[disney_plus_overall['type'] == 'Movie'].shape[0]  # 計算 'type' 列為 'Movie' 的行數
# num_shows = disney_plus_overall[disney_plus_overall['type'] == 'TV Show'].shape[0]  # 計算 'type' 列為 'TV Show' 的行數

# print(f"Number of Movies: {num_movies}")  # 輸出電影的數量
# print(f"Number of TV Shows: {num_shows}")  # 輸出電視節目的數量


# # # 繪製長條圖
# # sns.set(style="whitegrid")  # 設定 Seaborn 的繪圖樣式為 "whitegrid"，這會影響圖表的背景網格樣式，使其更適合呈現統計數據
# # ax = sns.countplot(x="type", data=disney_plus_overall, palette="Set2")  # 使用 Seaborn 的 countplot 函數繪製柱狀圖，x 軸為 "type" 欄位，數據來源為 disney_plus_overall，使用 "Set2" 調色盤
# # plt.title("Comparison of Movie vs TV Show on Disney_plus")  # 設置圖表標題
# # plt.xlabel("Type")  # 設置 x 軸標籤
# # plt.ylabel("Count")  # 設置 y 軸標籤

# # # 在長條圖上顯示統計數字
# # for p in ax.patches:  # 遍歷每個柱狀圖的 patch（即每個柱子）
    # # height = p.get_height()  # 獲取柱子的高度，即統計數字
    # # ax.text(p.get_x() + p.get_width() / 2., height + 10,  # 在柱子上方添加文本標籤，位置略高於柱子的頂端
            # # f'{int(height)}',  # 顯示的數字，轉換為整數
            # # ha='center',  # 水平對齊方式為中心
            # # va='bottom')  # 垂直對齊方式為底部

# # # 保存圖片
# # plot_file = os.path.join('reports', 'collect_data', 'D_type.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑，包含目錄路徑 'reports/collect_data' 和文件名 'N_type.png'
# # os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# # plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑

# # plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用
# # print(f"分析圖已保存到 {plot_file} 文件中。")  # 輸出一條消息到終端，告知用戶圖表已成功保存到指定的文件路徑


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
# plt.title("Proportion of Movies vs TV Shows on Disney_plus")  # 設置圖表標題

# # 保存圓餅圖
# plot_file_pie = os.path.join('reports', 'collect_data', 'D_type_pie_chart.png')  # 圓餅圖的儲存路徑
# os.makedirs(os.path.dirname(plot_file_pie), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# plt.savefig(plot_file_pie)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用
# print(f"圓餅圖已保存到 {plot_file_pie} 文件中。")  # 輸出一條消息到終端，告知用戶圖表已成功保存到指定的文件路徑



# 分析上架日期（'date_add'列），並產生圖表（影片更新頻率熱力圖）


# 確保 'date_added' 列是日期時間格式，並處理格式不一致的情況
disney_plus_overall['date_added'] = pd.to_datetime(disney_plus_overall['date_added'], errors='coerce')
# print(disney_plus_overall['date_added'])


# 提取年份和月份
disney_plus_date = disney_plus_overall[['date_added']].dropna()  # 從 disney_plus_overall 中提取 'date_added' 列，並刪除空值
disney_plus_date['year'] = disney_plus_date['date_added'].dt.year  # 提取年份
disney_plus_date['month'] = disney_plus_date['date_added'].dt.month_name()  # 提取月份名稱

# # 檢查創建的列
# print(disney_plus_date.head())
# print(disney_plus_date.columns)

# 計算每個年份中各個月份的頻次
month_counts = disney_plus_date.groupby('year')['month'].value_counts()  # month_counts 將會是一個 Series，其中包含每個年份和月份的計數，索引是 MultiIndex，第一層是年份，第二層是月份。
year_counts = disney_plus_date['year'].value_counts().sort_index()  # year_counts 將會是一個 Series，計算每個年份的總和。
# print(month_counts)
# print(year_counts)

# 定義月份順序，並反轉順序
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  #[::-1]
# print(month_order)

# 排列為矩陣
matrix = month_counts.unstack()  # 先使用 unstack() 將月份從行索引轉為列索引，未出現的月份會變成 NaN
matrix = matrix.fillna(0)  # 使用 fillna(0) 將 NaN 值填充為 0
matrix = matrix.astype(int)  # 將數據類型轉換為整數
matrix = matrix[month_order]  # 根據指定的月份順序重新排序列
result = matrix.T  # 將矩陣轉置，讓年份成為列索引，月份成為行索引
# print(result)

# # 計算年和月的總和

# result['Month Total'] = result.sum(axis=1)  # 計算每年的總和，並將結果新增至 DataFrame 的新列 'Year Total'
# result.loc['Year Total'] = result.sum(axis=0)  # 計算每月的總和，並將結果新增至 DataFrame 的新行 'Month Total'


# # 繪製表格

# # 設置圖表大小和分辨率
# plt.figure(figsize=(10,8), dpi=300)
# # plt.figure(): 創建一個新的圖形對象，這是 Matplotlib 用來顯示和處理圖形的容器。
# # figsize=(12, 8): 設定圖形的尺寸。figsize 是一個元組，表示圖形的寬度和高度，單位是英寸（inches）。
# # dpi=200: 設定圖形的解析度。dpi 代表 "dots per inch"（每英寸點數），它決定了圖形的解析度。在這個例子中，dpi=200 表示每英寸有 200 個點，這將使圖形的細節更為清晰。高 dpi 值通常用於生成高質量的圖像文件。

# table = plt.table(cellText=result.values,  # cellText：表格中的數據
                #   rowLabels=result.index,  # rowLabels：表格的行標籤
                #   colLabels=result.columns,  # colLabels：表格的列標籤
                #   cellLoc='center',  # cellLoc：表格單元格中文字的位置
                #   loc='center')  # loc：表格在圖中的位置

# # 設置表格樣式
# table.auto_set_font_size(True)  # 自動調整字體大小
# table.set_fontsize(8)  # 設置字體大小
# table.scale(1, 1)  # 調整表格的縮放比例

# # 繪製格線（使用 table 的內建方法）
# for key, cell in table.get_celld().items():  # 遍歷表格中的所有單元格，返回的 key 是單元格的行列索引，cell 是單元格對象
    # if key[0] in result.index and key[1] in result.columns:  # 檢查單元格的行和列是否在結果的索引和列中
        # cell.set_edgecolor('black')  # 設置單元格邊框顏色為黑色
        # cell.set_linewidth(0.05)  # 設置單元格邊框的線寬

# # 隱藏坐標軸
# plt.axis('off')

# # 保存表格為圖片
# plt_file_count_table = os.path.join('reports', 'collect_data', 'D_date_add_count_table.png')  # 表格的儲存路徑
# os.makedirs(os.path.dirname(plt_file_count_table), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# plt.savefig(plt_file_count_table, bbox_inches='tight')  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用


# # 繪製熱力圖
# plt.figure(figsize=(10, 7), dpi=200)  # 設置圖表大小和分辨率
# plt.pcolor(result, cmap='afmhot_r', edgecolors='white', linewidths=2)  # 使用顏色地圖繪製熱力圖
# plt.xticks(np.arange(0.5, len(result.columns), 1), result.columns, fontsize=7, fontfamily='serif')  # 設置 x 軸標籤
# plt.yticks(np.arange(0.5, len(result.index), 1), result.index, fontsize=7, fontfamily='serif')  # 設置 y 軸標籤
# plt.title('disney_plus Contents Update', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))  # 設置圖表標題
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
# plt_file_count_heatmap = os.path.join('reports', 'figures', 'D_date_add_heatmap.png')  # 表格的儲存路徑
# os.makedirs(os.path.dirname(plt_file_count_heatmap), exist_ok=True)  # 創建圖片儲存目錄（如果不存在的話）
# plt.savefig(plt_file_count_heatmap)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用


# 分別計算 "TV Show" 和 "Movie" 的 year_counts
tv_show_date = d1[['date_added']].dropna()  # 提取 "TV Show" 的 "date_added" 列，並刪除空值
tv_show_date['date_added'] = pd.to_datetime(tv_show_date['date_added'], format='%Y/%m/%d')  # 確保 'date_added' 列是日期時間格式
tv_show_date['year'] = tv_show_date['date_added'].dt.year  # 提取年份
tv_show_year_counts = tv_show_date['year'].value_counts().sort_index()  # 計算每年 "TV Show" 的數量並排序

movie_date = d2[['date_added']].dropna()  # 提取 "Movie" 的 "date_added" 列，並刪除空值
movie_date['date_added'] = pd.to_datetime(movie_date['date_added'], format='%Y/%m/%d')  # 確保 'date_added' 列是日期時間格式
movie_date['year'] = movie_date['date_added'].dt.year  # 提取年份
movie_year_counts = movie_date['year'].value_counts().sort_index()  # 計算每年 "Movie" 的數量並排序

# print(tv_show_year_counts)
# print(movie_year_counts)


# 繪製年分柱狀圖
# plt.figure(figsize=(12, 10))  # 設置圖表大小
# sns.set(style="whitegrid")  # 設置 Seaborn 的樣式為 "whitegrid"
# ax = sns.countplot(
    # x="year", 
    # data=disney_plus_date, 
    # color="#baf4ff", 
    # order=year_counts.index
# )  # 使用 Seaborn 繪製柱狀圖，顯示每年發布的電影數量，並按年份排序
# ax.set_title("Frequency of Content Added by Year", fontsize=16)  # 設置圖表標題
# ax.set_xlabel("Year", fontsize=14)  # 設置 x 軸標籤
# ax.set_ylabel("Number of Contents Added", fontsize=14)  # 設置 y 軸標籤
# plt.xticks(rotation=45)  # 將 x 軸上的刻度標籤旋轉 45 度
# plt.show()


# # 繪製雙折線圖
# plt.figure(figsize=(10, 6))

# # 繪製 "TV Show" 的年份數據，設定顏色為藍色
# plt.plot(tv_show_year_counts.index, tv_show_year_counts.values, label='TV Show', color='#E50611', marker='o')

# # 繪製 "Movie" 的年份數據，設定顏色為橙色
# plt.plot(movie_year_counts.index, movie_year_counts.values, label='Movie', color='#000000', marker='o')

# # 添加圖表標題和軸標籤
# plt.title('Yearly Counts of TV Shows and Movies')
# plt.xlabel('Year')
# plt.ylabel('Count')

# # 顯示圖例
# plt.legend()

# # 顯示網格線
# plt.grid(True)

# # 顯示圖表
# plt.show()


# 繪製組合圖


# 確保所有年份都在同一範圍內
years = sorted(set(tv_show_year_counts.index).union(movie_year_counts.index))

# 將缺失的年份填充為 0
tv_show_year_counts = tv_show_year_counts.reindex(years, fill_value=0)
movie_year_counts = movie_year_counts.reindex(years, fill_value=0)

# 計算總和年增長量
total_year_counts = tv_show_year_counts + movie_year_counts

# 創建圖表和第一個子圖（長條圖）
fig, ax1 = plt.subplots(figsize=(12, 8))

# 繪製長條圖，顯示 TV Shows 和 Movies 的總和年增長量
ax1.bar(years, total_year_counts, color='#baf4ff', alpha=0.6, label='Total Contents')

# 設置第一個子圖的標題和 X 軸標籤
ax1.set_title('Yearly Growth of TV Shows and Movies on Disney+')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Number of Contents', color='tab:blue')

# 設置 X 軸的刻度僅顯示整數年份
ax1.set_xticks(years)

# 設置 Y 軸的刻度顏色
ax1.tick_params(axis='y', labelcolor='tab:blue')

# 創建第二個共享 X 軸的子圖
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Contents', color='black')

# 設置相同的 Y 軸範圍
ax1_ylim = ax1.get_ylim()
ax2.set_ylim(ax1_ylim)

# 繪製雙折線圖
ax2.plot(years, tv_show_year_counts, label='TV Shows', color='#002034', marker='o', alpha=0.75)
ax2.plot(years, movie_year_counts, label='Movies', color='#005667', marker='o', alpha=1)

# 設置第二個 Y 軸的顏色
ax2.tick_params(axis='y', labelcolor='black')

# 添加圖例
ax2.legend(loc='upper left')

# 保存圖表
output_path = os.path.join('reports', 'figures', 'D_Yearly Growth of TV Shows and Movies.png')  # 設定儲存路徑
plt.savefig(output_path, format='png', bbox_inches='tight')  # 保存圖片

# 顯示圖表
plt.show()



# 分析發行年分（'release_year'列），並產生圖表


# 計算每年的電影數量
release_year_counts = disney_plus_overall['release_year'].value_counts().sort_index()
# print(release_year_counts)

# 根據數量降冪排序
release_year_counts_sorted = release_year_counts.sort_values(ascending=False)
# print(release_year_counts_sorted)


# # 繪製長條圖
# plt.figure(figsize=(12,10)) # 設置圖表大小
# sns.set(style="whitegrid") # 設置 Seaborn 的樣式為 "whitegrid"
# ax = sns.countplot(y="release_year", data=disney_plus_overall, palette="Set2", order=release_year_counts_sorted.index[0:15]) # 取前 15 名發行數量較多的年分，使用 Seaborn 繪製柱狀圖，顯示每年發布的電影數量，並按年份排序
# ax.set_title("Number of Movies Released by Disney+ Each Year", fontsize=16)  # 設置圖表標題

# # 將統計數字顯示在長條圖上
# for container in ax.containers:  # 使用迴圈來依次訪問每根長條
    # ax.bar_label(container, fmt='%d', label_type='edge', padding=3)  # 在當前長條上添加數字標籤
    # # fmt='%d': 指定標籤的格式為整數
    # # label_type='edge': 將標籤顯示在長條的邊緣
    # # padding=3: 設定標籤與條形之間的間距為3個像素

# # 保存圖片
# plot_file = os.path.join('reports', 'collect_data', 'D_release_year_bar.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑
# os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用


# # 繪製圓餅圖
# plt.figure(figsize=(8,8))  # 設置圖表大小
# top_years = release_year_counts_sorted.head(15)  # 取電影發布前15名多的年份
# # top_years_sorted = top_years.sort_index()  # 依照年份排序 
# plt.pie(
    # top_years,  # 圓餅圖的數據，即每個部分的數量或比例
    # labels=top_years.index,  # 每個扇形的標籤，這裡是年份
    # autopct='%1.0f%%',  # 顯示每個扇形的百分比，格式為整數的百分比
    # colors=sns.color_palette("Set2", 15),  # 設定圓餅圖的顏色，這裡使用 Seaborn 的 "Set2" 調色板，包含15種顏色
    # startangle=140  # 設置圓餅圖的起始角度為140度，以調整圖形的顯示方向
# )
# plt.title('Percentage of Disney+ Released Each Year')  # 設置圓餅圖標題

# # 保存圖片
# plot_file = os.path.join('reports', 'collect_data', 'D_release_year_pie.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑
# os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑
# plt.show()  # 顯示圓餅圖


# # 分析年齡分級（'rating'列），並產生圖表


# 計算年齡分級的電影數量
rating_counts = disney_plus_overall['rating'].value_counts().sort_index()
# print(rating_counts)


# # 繪製長條圖
# plt.figure(figsize=(12,10)) # 設置圖表大小
# sns.set(style="whitegrid") # 設置 Seaborn 的樣式為 "whitegrid"
# ax = sns.countplot(x="rating", data=disney_plus_overall, palette="Set2", order=rating_counts.index) # 使用 Seaborn 繪製柱狀圖，顯示影片分級的數量分布
# ax.set_title("Distribution of Disney+ Movies by Rating", fontsize=16)  # 設置圖表標題

# # # 將統計數字顯示在長條圖上
# for container in ax.containers:  # 使用迴圈來依次訪問每根長條
    # ax.bar_label(container, fmt='%d', label_type='edge', padding=3)  # 在當前長條上添加數字標籤
    # # fmt='%d': 指定標籤的格式為整數
    # # label_type='edge': 將標籤顯示在長條的邊緣
    # # padding=3: 設定標籤與條形之間的間距為3個像素

# # 保存圖片
# plot_file = os.path.join('reports', 'collect_data', 'D_rating_bar.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑
# os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑

# plt.show()  # 顯示當前圖表，使其在螢幕上顯示出來，這對於交互式環境特別有用


# # 繪製圓餅圖
# plt.figure(figsize=(8,8))  # 設置圖表大小
# plt.pie(
    # rating_counts,  # 圓餅圖的數據，即每個部分的數量或比例
    # labels=rating_counts.index,  # 每個扇形的標籤，這裡是年份
    # autopct='%1.0f%%',  # 顯示每個扇形的百分比，格式為整數的百分比
    # colors=sns.color_palette("Set2", 15),  # 設定圓餅圖的顏色，這裡使用 Seaborn 的 "Set2" 調色板，包含15種顏色
    # startangle=140  # 設置圓餅圖的起始角度為140度，以調整圖形的顯示方向
# )
# plt.title('Percentage Distribution of Disney+ by Rating')  # 設置圓餅圖標題

# # 保存圖片
# plot_file = os.path.join('reports', 'collect_data', 'D_rating_pie.png')  # 使用 os.path.join 函數組合成圖片的儲存路徑
# os.makedirs(os.path.dirname(plot_file), exist_ok=True)  # 使用 os.makedirs 創建圖片儲存目錄（如果不存在的話），exist_ok=True 表示如果目錄已經存在則不報錯
# plt.savefig(plot_file)  # 使用 plt.savefig 函數將當前的圖表保存到指定的文件路徑

# plt.show()  # 顯示圓餅圖