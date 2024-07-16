import pandas as pd
import os
from utils.data_utils import preprocess_data, save_data



# 定義數據文件路徑

raw_data_path = os.path.join('data', 'raw', 'netflix.csv')
processed_data_path = os.path.join('data', 'processed', 'netflix_cleaned.csv')

    # 透過 os.path.join() 函式將導入文件路徑，這個方法具有話平台的兼容性