# AI 驅動的串流平台選擇系統：為 Netflix 和 Disney+ 提供深度推薦
### AI-Driven Streaming Platform Selection System: In-Depth Recommendations for Netflix and Disney+

---

本專案是一個基於 Streamlit 的影片推薦系統，旨在幫助用戶比較並選擇適合的影片串流平台（如 Netflix 和 Disney+），以滿足其個人觀看偏好和預算考量。系統利用數據分析和視覺化工具展示兩大平台的影片類型分佈、受歡迎程度，並推薦符合用戶偏好的影片。    

+ 平台網址：https://pickyourstreambetweennetflixanddisneyplus.streamlit.app/  
+ 或點此 [🌐](https://pickyourstreambetweennetflixanddisneyplus.streamlit.app/) 進入平台

## 專案概述
目前在台灣，有提供合法的影片串流平台主要是 Disney+ 和 Netflix。若消費者預算有限，只能訂購一個平台，可以透過本專案的分析方向，提供消費者訂閱參考，並在最後運用「影片類型」選單，結合 Disney+ 和 Netflix 現有的影片，依據消費者的觀影喜好，生成推薦片單。 

## 功能分析

## 頁面展示

## 專案結構

```bash
stream_AI_advisor
│
└── data
│   ├── data_SQLite                        # SQLite 資料庫文件
│   │   ├── disney.db                      # Disney+ 資料庫
│   │   └── netflix.db                     # Netflix 資料庫
│   ├── processed                          # 處理後的數據資料夾
│   └── raw                                # 原始數據資料夾
│
├── reports
│   └── collect_data
│       ├── Disney                         # Disney+ 數據相關文件
│       ├── Netflix                        # Netflix 數據相關文件
│       ├── D Content Description Keywords.xlsx
│       ├── N Content Description Keywords.xlsx
│       ├── N Co-occurrence Matrix of L.xlsx
│       └── cat_choose.png                 # 首頁圖片
│
└── src
    ├── streamlit_run                      # Streamlit 應用程式
    │   ├── pages                          # Streamlit 頁面模組
    │   │   ├── 1_📊_chart_view.py         # 圖表視覺化頁面
    │   │   ├── 2_🔍_search_movies.py      # 搜尋電影頁面
    │   │   ├── 3_📝_match_rate.py         # 配對率頁面
    │   │   ├── _init_.py                  # 初始化文件
    │   │   └── 🏠_Home.py                 # 主頁面
    │   └── _init_.py                      # 初始化文件
    │
    ├── utils                              # 工具模組
    │   ├── __init__.py                    # 初始化文件
    │   ├── data_keywords_D.npy            # Disney+ 關鍵詞數據
    │   ├── data_keywords_N.npy            # Netflix 關鍵詞數據
    │   ├── data_utils_mysql_D.py          # Disney+ MySQL 數據處理
    │   ├── data_utils_mysql_N.py          # Netflix MySQL 數據處理
    ├── data_sql_disney_plus.py            # Disney+ SQL 操作模組
    └── data_sql_netflix.py                # Netflix SQL 操作模組
```

## 資料來源
1. Netflix Movies and TV Shows  
https://www.kaggle.com/datasets/shivamb/netflix-shows/data  
2. Disney+ Movies and TV Shows  
https://kaggle.com/datasets/shivamb/disney-movies-and-tv-shows  

## 目標用戶
此系統適合希望通過數據分析來選擇最適影片串流平台的使用者，包括：
+ 追求影片類型多樣性與流行趨勢的用戶
+ 希望根據影片預算、觀看偏好來選擇平台的用戶
