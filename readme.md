# AI 驅動的串流平台選擇系統：為 Netflix 和 Disney+ 提供深度推薦
AI-Driven Streaming Platform Selection System: In-Depth Recommendations for Netflix and Disney+

---

本專案是一個基於 **Streamlit** 的影片推薦系統，旨在幫助用戶比較並選擇適合的影片串流平台（如 **Netflix** 和 **Disney+**），以滿足其個人觀看偏好和預算考量。  
系統利用數據分析和視覺化工具展示兩大平台的影片類型分佈、受歡迎程度，並推薦符合用戶偏好的觀影平台。    

+ 平台網址：https://pickyourstreambetweennetflixanddisneyplus.streamlit.app/  
+ 或點此 [🌐](https://pickyourstreambetweennetflixanddisneyplus.streamlit.app/) 進入平台
+ 或掃描QRcode進入平台：
  ![image](https://github.com/user-attachments/assets/2b73b0d7-170a-4062-9f98-722221cabe11)


## 專案概述
目前在台灣，主要是由 **Disney+** 和 **Netflix** 提供合法的影片串流平台。    
若消費者預算有限，只能訂購一個平台，可以透過本專案的分析方向，提供消費者訂閱參考，並在最後運用選單，結合 **Disney+** 和 **Netflix** 現有的影片，依據消費者的觀影喜好，生成推薦片單。 

## 功能分析
本系統提供一系列深入的比較分析，幫助用戶了解 **Netflix** 和 **Disney+** 兩大平台的影片內容差異。通過視覺化圖表以及圖片說明，用戶可以輕鬆比較兩平台在多個維度上的分佈情況。

### 1. 影片類型（type）比較：
+ 比較 **Netflix** 和 **Disney+** 收錄的各類影片類型，並呈現每個平台上不同類型影片的數量和比例。
+ 用戶可以直觀了解兩平台在影片類型上的多樣性，並根據自身偏好選擇平台。

### 2. 導演（director）比較：
+ 分析兩平台影片的導演分佈情況，展示每個平台導演的數量和影片數量。
+ 這一功能讓用戶了解兩大平台在影片製作上的導演差異，並幫助有特定導演偏好的觀眾作出選擇。

### 3. 卡司（cast）比較：
+ 比較 **Netflix** 和 **Disney+** 上影片中的卡司（演員）分佈，展示主要演員在各平台的影片中出現的頻率。
+ 這有助於用戶了解各平台的明星效應及演員吸引力。

### 4. 製作國家（country）比較：
+ 展示兩大平台的影片來自哪些國家，並比較每個平台上來自不同國家的影片數量。
+ 此功能適合有地域偏好的用戶，幫助他們選擇最符合自己文化背景或語言需求的影片。

### 5. 影片上架時間（date_added）分布：
+ 比較 **Netflix** 和 **Disney+** 上影片的上架時間，並展示影片上架的時間趨勢，以及不同影片類型的上架時間曲線。
+ 用戶可以查看每個平台影片的上架年份，了解平台影片的更新頻率。

### 6. 年齡分級（rating）分布：
+ 比較兩大平台影片的年齡分級分布，讓用戶了解每個平台上的影片適合哪些年齡層觀看。
+ 這一功能有助於家長或對年齡分級有需求的觀眾選擇合適的影片。

### 7. 影片時長（duration）分布：
+ 分析並比較 **Netflix** 和 **Disney+** 平台上影片的時長分佈情況。
+ 用戶可以查看每個平台上影片的長短，幫助他們選擇適合自己時間安排的影片。

### 8. 內容分類（listed_in）分布：
+ 比較 **Netflix** 和 **Disney+** 平台上影片的內容分類（例如：動作、喜劇、科幻等），展示每個平台的影片分類分佈情況。
+ 這對於有特定內容偏好的用戶來說非常有用，能夠快速找到自己喜愛的影片類型。

## 頁面展示
本專案開發的推薦系統，提供了四個主要頁面，包括首頁和三個分頁，分別呈現不同的功能與數據視覺化，幫助用戶比較 **Netflix** 和 **Disney+** 兩大平台的影片資源。

### 1. 首頁（🏠Home）：
+ 首頁作為系統的主頁，簡要介紹了專案的目標與功能，並提供導航至其他詳細頁面。用戶可以在此查看平台比較的基本介紹與連結。

### 2. 圖表檢視（📊chart view）：
+ 此頁面展示了 **Netflix** 和 **Disney+** 上影片各類型的數據分析結果。
+ 使用者可以透過視覺化圖表（如柱狀圖、圓餅圖等），直觀比較兩平台在各影片類型、年齡分級、影片長度等方面的分佈情況。
+ 該頁面主要是為了提供數據比較和視覺化展示，幫助用戶了解兩大平台影片資源的差異。

### 3. 搜尋電影（🔍search movies）：
+ 這一頁面允許使用者根據多種篩選條件進行電影搜尋。
+ 使用者可以設置條件，如影片類型、影片標題、導演、演員、製作國家、發行年分、年齡分級、影片時長、內容分類以及影片關鍵字等，並查看 **Netflix** 和 **Disney+** 平台中符合條件的電影詳細資訊。
+ 此功能對於希望根據特定需求搜尋電影的用戶特別有用，幫助他們精確找到自己感興趣的影片。

### 4. 適配比率（📝match rate）：
+ 此頁面提供了一個影片適配度的比較工具。
+ 用戶可以選擇篩選條件（如影片類型、影片標題、導演、演員等），系統將顯示 **Netflix** 和 **Disney+** 兩平台中符合條件的影片數量比例。
+ 這有助於用戶了解每個平台在符合其需求的影片範圍內的選擇比例，從而幫助使用者選擇最適合的觀影平台。

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

## 安裝與執行
1. Clone 本專案：

    ```bash
    git clone https://github.com/liaoxiaoxuan/stream_AI_advisor.git
    ```

2. 切換至專案目錄並安裝必要套件：

    ```bash
    cd stream_AI_advisor/src
    pip install -r requirements.txt
    ```

3. 啟動 Streamlit 應用程式：

    ```bash
    streamlit run app.py
    ```

4. 在瀏覽器中打開本地地址（預設為 `http://localhost:8501` ），開始使用推薦系統。

## 資料來源
1. Netflix Movies and TV Shows  
https://www.kaggle.com/datasets/shivamb/netflix-shows/data  
2. Disney+ Movies and TV Shows  
https://kaggle.com/datasets/shivamb/disney-movies-and-tv-shows  

## 目標用戶
此系統適合希望通過數據分析來選擇最適影片串流平台的使用者，包括：
+ 追求影片類型多樣性與流行趨勢的用戶
+ 希望根據影片預算、觀看偏好來選擇平台的用戶

## 成果與展望

本專案成功開發了一個基於 **Streamlit** 的電影推薦與比較系統，旨在幫助用戶比較 **Netflix** 和 **Disney+** 兩大串流平台的影片資源，並選擇適合平台訂閱。   

主要功能包括：  
1. 透過數據視覺化展示兩平台影片的類型分佈、年齡分級、影片長度等資訊。
2. 提供電影搜尋功能，幫助用戶篩選出符合需求的影片。
3. 提供平台之間的適配度比率，幫助用戶選擇最適合自己的串流平台。

這些功能通過清晰、直觀的頁面展示，讓用戶可以在兩大平台之間做出更明智的選擇。    
專案實現了多維度的數據分析，並有效幫助用戶理解平台上的影片資源差異。    

雖然本專案已經成功實現了主要的功能，但仍有一些改進和擴展的空間，未來可以考慮以下幾個方向：  
### 1. 增加更多過濾條件
目前的篩選條件主要集中在影片類型、導演、演員等基本資料，未來可以加入更多元化的條件，如用戶評分、觀影心得等，進一步提升搜尋精確度。  
### 2. 個性化推薦功能
基於用戶的觀看歷史或偏好，開發個性化的影片推薦系統，提供更符合用戶口味的推薦結果。  
### 3. 擴展平台覆蓋範圍
目前只針對 **Netflix** 和 **Disney+** 進行分析，未來可以考慮擴展到其他流行串流平台，如 **HBO GO** 、 **Apple TV+** 、 **myVideo** 和 **friDay 影音** 等，為用戶提供更廣泛的比較選擇。   
### 4. 提升數據更新頻率
目前的數據來源是靜態的，未來可以實現自動化數據抓取與更新，確保平台影片數據的時效性。    
### 5. 更多視覺化與交互功能
提升圖表的交互性，讓用戶能夠進一步探索數據細節，增加更多自定義視覺化選項，例如影片評分分布等圖表內容。  

這些改進和展望不僅能夠提高系統的準確性和使用者體驗，還能擴大其應用範圍，吸引更多的用戶使用。    
隨著技術的發展和數據來源的多樣化，這個專案有望在未來成為更強大且全面的影片推薦與比較工具。
