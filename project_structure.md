stream_ai_advisor/
│
├── data/
│   ├── raw/
│   │   ├── netflix.csv       # Netflix 原始數據文件
│   │   └── disney.csv        # Disney+ 原始數據文件
│   ├── processed/
│   │   ├── netflix_cleaned.csv  # 預處理後的 Netflix 數據文件
│   │   └── disney_cleaned.csv   # 預處理後的 Disney+ 數據文件
│
├── notebooks/
│
├── scripts/
│   ├── data_collection_netflix.py     # 收集 Netflix 數據
│   ├── data_collection_disney.py      # 收集 Disney+ 數據
│   ├── data_preprocessing_netflix.py  # 預處理 Netflix 數據
│   ├── data_preprocessing_disney.py   # 預處理 Disney+ 數據
│   ├── eda.py                         # 初步數據探索分析（EDA）
│   ├── data_analysis.py               # 數據分析
│   ├── nlp_analysis.py                # 自然語言處理與情感分析
│   ├── recommendation.py              # 推薦系統開發
│
├── reports/
│   ├── figures/
│   └── final_report.md
│
├── utils/
│   └── helper_functions.py
│
├── main.py  # 主程序，統合所有模組
├── requirements.txt
└── README.md
