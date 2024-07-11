stream_ai_advisor/  
│   
├── data/   
│   ├── raw/    
│   │   ├── netflix.csv       # Netflix 原始數據文件 Ｘ    
│   │   └── disney.csv        # Disney+ 原始數據文件 Ｘ    
│   ├── processed/  
│   │   ├── netflix_cleaned.csv  # 預處理後的 Netflix 數據文件 Ｖ  
│   │   └── disney_cleaned.csv   # 預處理後的 Disney+ 數據文件 Ｖ  
│   
├── notebooks/  
│   
├── scripts/    
│   ├── data_collection_netflix.py     # 收集 Netflix 數據 ⊙  
│   ├── data_collection_disney.py      # 收集 Disney+ 數據 ⊙  
│   ├── data_preprocessing_netflix.py  # 預處理 Netflix 數據 ⊙    
│   ├── data_preprocessing_disney.py   # 預處理 Disney+ 數據 ⊙    
│   ├── eda.py                         # 初步數據探索分析（EDA）    
│   ├── data_analysis.py               # 數據分析   
│   ├── nlp_analysis.py                # 自然語言處理與情感分析 
│   ├── recommendation.py              # 推薦系統開發   
│   
├── reports/             # 與報告相關的文件和圖表 
│   ├── figures/         # 專案中生成的所有視覺化圖表   
│   └── final_report.md  # 最終報告，包含專案的介紹、方法、結果和結論
│   
├── utils/                   # 專案中的輔助函數和工具   
│   └── helper_functions.py  # 包含各種輔助函數，比如讀取和寫入數據的函數、數據清理和處理的函數，還可能包括一些常見的數學或統計函數 
│   
├── main.py  # 主程序，統合所有模組 
├── requirements.txt    
└── README.md   
