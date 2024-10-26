import streamlit as st

import numpy as np
import pandas as pd

import os
from PIL import Image



# 分頁容器標籤
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
   ["說明", "影片類型", "導演", "演員", "製作國家", "上架日期", "年齡分級", "時長", "內容分類"]
   )


with tab1:
    st.header("資料來源與簡介")
    st.subheader("Data Sources and Overview")
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content type Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 影片類型數量")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Type Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 影片類型數量")
    st.write(
        """
        - 關於 `chart_view` 這部分，是供使用者閱覽 `Netflix` 和 `Disney+` 這兩個串流平台部分數據的可視化分析結果。
        - 數據來源主要是以下兩個網站：
        1. Netflix Movies and TV Shows　https://www.kaggle.com/datasets/shivamb/netflix-shows/data
        2. Disney+ Movies and TV Shows　https://kaggle.com/datasets/shivamb/disney-movies-and-tv-shows
        - 從上方兩張引圖，大抵可以了解：
        1. 無論是在哪個平台，`Movie` 的數量都是多過於 `TV Show`。
        2. 在總數上，`Netflix` 又多過於 `Disney+`，最主要的原因是，`Netflix` 的數據資料是從 2008 至 2021，而 `Disney+` 則是從 2019 至 2021，因為資料量的不同所產生的落差。
        """)


with tab2:
    st.header("比較 Netflix 和 Disney+ 影片類型")
    st.subheader("The comparison of movie genres between Netflix and Disney+")
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Type Distribution pie.png")
    st.image(image_N_bar_type, caption="Netflix 影片類型佔比")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Type Distribution pie.png")
    st.image(image_D_bar_type, caption="Disney+ 影片類型佔比")
    st.write(
        """
        `Netflix` 和 `Disney+` 兩平台，`Movie` 的比例較 `TV Show` 多出一倍，佔平台總量的三分之二。
        """)


with tab3:
    st.header("比較 Netflix 和 Disney+ 收錄影片的導演")
    st.subheader("Comparison of Directors Featured in Netflix and Disney+ Movies")
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Director Multi_label Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 收錄影片，參與指導數量前 15 名的導演")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Director Multi_label Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 收錄影片，參與指導數量前 15 名的導演")
    st.write(
        """
        - 由於兩平台收錄的影片導演眾多，因此僅以出現次數前 15 多的導演進行可視化呈現，並顯示其在平台上執導的影片數量。
        - 在 `Netflix` 上，由動畫師 `Rajiv Chilaka` 負責執導或參與導演的影片，收錄量最多，有 22 部；而有多部影史經典的著名導演 `Steven Spielberg`，則有 11 部影片被 `Netflix` 收錄。
        - 在 `Disney+` 上，則是 `Jack Hannah` 負責執導或參與導演的影片拔得頭籌，總共有 17 部，其代表作有《奇奇蒂蒂》。
        """)


with tab4:
    st.header("比較 Netflix 和 Disney+ 收錄影片的卡司")
    st.subheader("Comparison of Directors Featured in Netflix and Disney+ Movies")
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Cast Multi_label Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 收錄影片，參與演出數量前 15 名的卡司")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Cast Multi_label Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 收錄影片，參與演出數量前 15 名的卡司")
    st.write(
        """
        - 由於兩平台收錄的影片演員眾多，因此僅以出現次數前 15 多的演員進行可視化呈現，並顯示其在平台上出演的影片數量。
        - 在 `Netflix` 上，由印度男演員 `Anupam Kher` 出演的影片，收錄量最多，有 39 部。
        - 在 `Disney+` 上，則是由美國配音員 `Jim Cummings` 參與演出的影片拔得頭籌，總共有 24 部，其代表作有《獅子王》、《史瑞克》等。
        """)


with tab5:
    st.header("比較 Netflix 和 Disney+ 收錄影片的製作國家")
    st.subheader("Comparison of Production Countries for Movies Featured in Netflix and Disney+")
    st.write(
        """
        - 由於兩平台收錄影片的製作國家眾多，因此僅以出現次數前幾名的國家進行可視化呈現。
        """)
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Country Multi_label Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 收錄影片，製作影片前幾名的國家")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Country Multi_label Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 收錄影片，製作影片前幾名的國家")
    st.write(
        """
        - 無論是在 `Netflix` 或是 `Disney+`，都是由美國（U. S. ）所製作或參與製作的影片佔大宗，且遠遠超過其他國家的數量，但第二和第三則有所不同。
        - 在 `Netflix` ，第二多的是印度（India）所參與製作的電影，第三則是英國（U. K. ）。
        - 在 `Disney+` ，第二多的是英國（U. A. ）所參與製作的電影，第三則是加拿大（Canada）。
        """)
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Country Combo_Counts Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 收錄影片，共同參與製作影片前幾名的國家組合")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Country Combo_Counts Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 收錄影片，共同參與製作影片前幾名的國家組合")
    st.write(
        """
        - 即使是共同製作的國家組合，依然可見 `Netflix` 或 `Disney+` 都是美國（U. S. ）獨立製作的電影佔最大宗。
        - 在 `Netflix` 上，第二和第三也是由印度（India）和英國（U. K. ）獨立製作的電影包攬；若從圖表上來看，合作製作的電影佔多數的，首先是英國（U. K. ）和美國（U. S. ），其次是加拿大（Canada）和美國（U. S. ）。
        - 在 `Disney+` 上，第二和第三則分別是美、英和美、加共同製作的影片，至於英國（U. K. ）獨立製作的則降至第四。
        - 綜合來看，和前面兩張圖表不同的是，即使從「共同製作」的角度來分析， `Netflix` 平台較多單一國家製作的影片，但 `Disney+` 多為美國（U. S. ）和他國合作的作品。
        """)
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N _Co-occurrence Matrix of Labels by Country.png")
    st.image(image_N_bar_type, caption="以「共獻矩陣」呈現 Netflix 收錄影片，共同參與製作影片前幾名的國家組合")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D _Co-occurrence Matrix of Labels by Country.png")
    st.image(image_D_bar_type, caption="以「共獻矩陣」呈現 Disney+ 收錄影片，共同參與製作影片前幾名的國家組合")
    st.write(
        """
        - 和柱狀圖不同的是，「共獻矩陣」較能多元呈現國家之間的合作情形。
        """)
    

with tab6:
    st.header("Netflix 和 Disney+ 影片上架時間分布")
    st.subheader("The distribution of release times for shows on Netflix and Disney+")

    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N content addition heatmap.png")
    st.image(image_N_bar_type, caption="以「共獻矩陣」呈現 Netflix 影片上架時間（包含年、月）")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D content addition heatmap.png")
    st.image(image_D_bar_type, caption="以「共獻矩陣」呈現 Disney+ 影片上架時間（包含年、月）")
    st.write(
        """
        - 在 `Netflix` 的上架情形，從 2018 開始，影片數量有著顯著的成長，尤其是 2019/11 和 2021/7 上架數量最多。
        - 在 `Disney+` 的上架情形，影片的上架數量平均成長，唯有 2019/11 有突破性的新增數，高達 730 部之多，這恰好也是 `Disney+` 平台的推出時間。
        """)

    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Yearly Growth of TV Shows and Movies on Netflix.png")
    st.image(image_N_bar_type, caption="以組合圖呈現 Netflix 影片數量成長")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Yearly Growth of TV Shows and Movies on Disney+.png")
    st.image(image_D_bar_type, caption="以組合圖呈現 Disney+ 影片數量成長")
    st.write(
        """
        - 綜合而言，兩平台的成長數量，長期都是 `Movie` 較 `TV Show` 來得多；但整體來看， `Netflix` 較有持續、穩定的成長。
        - 從組合圖來看， `Netflix` 從 2016 開始，影片數量就有上升趨勢，直到 2019 達高峰。
        - 在 `Disney+` 的上架情形，則是 2019 平台推出當年，上架最多影片，而後兩年，影片成長數量都僅約首年的一半。
        """)


with tab7:
    st.header("Netflix 和 Disney+ 影片的年齡分級分布")
    st.subheader("The age rating distribution of shows on Netflix and Disney+")
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Rating Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 影片的年齡分級分布")
    st.write(
        """
        1. 從整體柱狀圖來看，`Netflix` 收錄的影片，年齡分級最多的是 `TV-MA`，意即「為了成年觀眾而製作，因此可能有些內容不適合年齡低於 17 歲的兒童」；其次是 `TV-14`，也就是內容「包含家長可能認為不適合年齡低於 14 歲兒童的內容」；收錄數量第三多的也是 TV Show 當中的 `TV-PG`，內容「可能會讓部分家長感到不適合 8 歲以下兒童觀看，部分片段可能會有輕度驚嚇，輕度暴力，或輕度性暗示，但大部分內容適合兒童觀看」。
        2. 若把電影分級獨立出來看，當中收錄最多的是 `R`（限制級），「17歲以下必須由父母或者監護陪伴才能觀看」；其次是 `PG-13`（特別輔導級），「13 歲以下建議要有父母陪同觀看，一些內容對兒童很不適宜」，內容雖然「沒有粗野的持續暴力鏡頭，一般沒有裸體鏡頭」，但「有時會有吸毒鏡頭和髒話」。
        """)
    
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Rating Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 影片的年齡分級分布")
    st.write(
        """
        1. 從整體柱狀圖來看，`Disney+` 收錄的影片，年齡分級最多的是 `TV-G`，意即「大多數的家長會認為此節目適合所有年齡」；其次是 `TV-PG`，也就是內容「可能會讓部分家長感到不適合8歲以下兒童觀看，部分片段可能會有輕度驚嚇，輕度暴力，或輕度性暗示，但大部分內容適合兒童觀看」。
        2. 若把電影分級獨立出來看，當中收錄最多的是 `G`（大眾級），「所有年齡均可觀看」；其次是 `PG`（普通輔導級），「一些內容可能不適合兒童觀看，有些鏡頭可能產生不適感，建議在父母的陪伴下觀看」，和  `PG-13` 不同的是，`PG` 的內容「基本沒有性愛、吸毒和裸體場面，即使有時間也很短，此外，恐怖和暴力場面不會超出適度的範圍」。
        
        - - -
        - 綜合而言
        1. `Disney+` 適合觀賞的年齡層較為廣泛，收錄的大多是闔家觀賞的影片，特別是嬰幼兒少的觀影需求。
        2. `Netflix` 收錄的影片，適合觀看年齡偏向青少年以上的閱聽眾。
                
        - - -
        - 年齡分級參考資料：
        1. 美國電視分級制度　https://zh.wikipedia.org/zh-tw/%E7%BE%8E%E5%9B%BD%E7%94%B5%E8%A7%86%E5%88%86%E7%BA%A7%E5%88%B6%E5%BA%A6#
        2. 電影分級制度（美國）　https://zh.wikipedia.org/zh-tw/%E9%9B%BB%E5%BD%B1%E5%88%86%E7%B4%9A%E5%88%B6%E5%BA%A6#%E7%BE%8E%E5%9B%BD
        """)


with tab8:
    st.header("Netflix 和 Disney+ 影片的時長分布")
    st.subheader("The duration distribution of shows on Netflix and Disney+")
    st.write(
        """
        - 考量 `TV Show` 和 `Movie` 影片時長計算單位的差異，在「影片時長分布」這部分，將 `TV Show` 和 `Movie` 分開說明。
        1. `TV Show` 是以「季 `season`」為單位
        2. `Movie` 是以「分鐘 `min`」為單位
        - 此外，兩平台的時長記錄瑣碎且數量龐大，尤其是 `Movie` 的資料，因此該部分的分析以 `分組` 的方式加以計數、統計和可視化呈現。
        """)
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Movie Duration Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 電影時長分布")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Movie Duration Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 電影時長分布")
    st.write(
        """
        - 兩平台收錄的 `Movie` 時長分布相似，最多的都是 `90~120 分鐘` 的電影，其次是 `60~90 分鐘`，第三名才有差異：
        1. `Netflix` 是 `120~150 分鐘`。
        2. `Disney+` 則是 `40~60 分鐘`。
        - 整體來看，`150 分鐘` 以上的電影，在兩平台的收錄量都比較少，`120 分鐘` 以下的影片佔多數。
        """)

    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content TV Show Duration Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 影集時長分布")
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content TV Show Duration Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 影集時長分布")
    st.write(
        """
        - 無獨有偶，兩平台收錄的 `TV Show` 時長分布，也有高度的相似性，都是 `1 至 2 季` 的電視節目收錄量最為突出，其次是 `2 至 3 季`，第三名才是 `3 至5 季`。
        - 整體來看，5 季長度以內的電視節目，收錄量最多，尤其 `1 至 2 季` 的電視節目佔比最高，5 季以上收錄數量大幅降低，11 季以上近乎為零。
        """)


with tab9:
    st.header("Netflix 和 Disney+ 影片內容分類分布")
    st.subheader("The content category distribution of shows on Netflix and Disney+")
    st.write(
        """
        - 從原始資料來看，一部影片通常不會只被歸為一項類別，可能是多元的組成類別，惟以下可視化圖表，僅計算單一類別的出現次數。
        - 兩平台影片內容分類的類別繁多，在此僅以出現次數 `前 15 名` 進行可視化呈現。
        """)
    
    image_N_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Netflix/N Content Listed_in Multi_label Distribution bar.png")
    st.image(image_N_bar_type, caption="Netflix 影片內容分類")
    st.write(
        """
        - 直觀來看，`Netflix` 平台上，`International Movies` 類型出現次數最多，其次則是 `戲劇 Drama` 和 `喜劇 Comedies`，有趣的是前 3 名都是 `Movies` 的類別，大概是 `Movies` 的收錄量本身就比 `TV Show` 多。
        - 直到第 4 名才有 `TV Show` 的類別 `International Movies` 上榜，而後一直要到第 7 與第 8 才有 `TV Show` 的類別，分別是 `TV Drama` 和 `TV Comedies`，類型與 `Movies` 前 3 名相同。
        """)
    
    image_D_bar_type = Image.open(r"/mount/src/stream_ai_advisor/reports/collect_data/Disney/D Content Listed_in Multi_label Distribution bar.png")
    st.image(image_D_bar_type, caption="Disney+ 影片內容分類")
    st.write(
        """
        - `Disney+` 的資料，不像 `Netflix` 有特別註明、區分 `TV Show` 和 `Movies`。
        - 整體來看，在 `Disney+` 平台上，`家庭 Family`、`卡通 Animation`、`喜劇 Comedy` 和 `動作冒險 Action-Adventure` 數量最多，分別位居前四名。
        """)




