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
│   ├── data_processing_netflix.py       # 收集和預處理 Netflix 數據    
│   ├── data_processing_disney.py        # 收集和預處理 Disney+ 數據    
│   ├── eda_netflix.py                   # Netflix 初步數據探索分析（EDA）  
│   ├── eda_disney.py                    # Disney+ 初步數據探索分析（EDA）  
│   ├── data_analysis.py                 # 數據分析和比較   
│   ├── nlp_analysis.py                  # 自然語言處理與情感分析   
│   ├── recommendation.py                # 推薦系統開發  
│   
├── utils/  
│   ├── data_utils.py                    # 數據處理和預處理的共用函數   
│   ├── analysis_utils.py                # 數據分析的共用函數   
│   
├── config/     
│   ├── config.yaml                      # 配置文件，包含路徑和參數     
│   
├── reports/             # 與報告相關的文件和圖表   
│   ├── collect_data/    # data 數據   
│   ├── figures/         # 專案中生成的所有視覺化圖表   
│   └── final_report.md  # 最終報告，包含專案的介紹、方法、結果和結論   
│   
├── main.py  # 主程序，統合所有模組     
├── requirements.txt    
└── README.md   
