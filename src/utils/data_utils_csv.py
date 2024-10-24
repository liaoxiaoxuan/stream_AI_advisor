# 數據處理和預處理的共用函數

import pandas as pd



# 預處理

def preprocess_data(data):
    data.drop_duplicates(inplace=True)
    # 刪除數據中的重複行
    data.fillna('NA', inplace=True)
    # 將所有缺失值填充為 'NA'
    return data



# 儲存至 CSV

def save_data(data, path):
    data.to_csv(path, index=False)
    # 將數據保存為 CSV 
    # index=False 表示不將索引列保存到文件中

