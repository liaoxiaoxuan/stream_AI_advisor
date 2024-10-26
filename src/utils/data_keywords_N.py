import mysql.connector
import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tqdm import tqdm
import os
from dotenv import load_dotenv



# 定義一個函數來從文本中提取 TF-IDF 關鍵詞
def extract_keywords_tfidf(tfidf_matrix, feature_names, num_keywords=5):
    doc_index = tfidf_matrix.getrow(-1)  # 取出最新一行（即當前文本）的 TF-IDF 向量
    doc_weights = doc_index.toarray().flatten()  # 將稀疏矩陣轉換為一維數組
    top_indices = doc_weights.argsort()[-num_keywords:][::-1]  # 按權重排序，選出前 num_keywords 個最高值
    return [feature_names[i] for i in top_indices]  # 返回對應的關鍵詞列表



# 定義一個處理電影摘要的函數
def process_movie_summaries(host=None, user=None, password=None, database=None, name='N', table_name='netflix_titles'):
    # 連接到MySQL數據庫
    # connection = mysql.connector.connect(
        # host = host or os.getenv(f'MYSQL_HOST_{name}'),
        # user = user or os.getenv(f'MYSQL_USER_{name}'),
        # password = password or os.getenv(f'MYSQL_PASSWORD_{name}'),
        # database = database or os.getenv(f'MYSQL_DATABASE_{name}')
    # )
    connection = sqlite3.connect(r"D:\PYTHON\oo_hank_project\stream_AI_advisor\data\data_SQLite\netflix.db")
    cursor = connection.cursor()


    # 讀取電影摘要
    query = f"SELECT show_id, description FROM {table_name}"  # SQL 查詢語句，從指定表中選取 id 和 summary 列
    df = pd.read_sql(query, connection)  # 使用 Pandas 從數據庫中讀取數據並存為數據框


    # 初始化TF-IDF向量器
    tfidf = TfidfVectorizer(stop_words='english', max_features=3000)  # 去除英文停用詞，最多保留 5000 個特徵


    # 擬合 TF-IDF 向量器並將摘要轉換為 TF-IDF 矩陣
    tfidf_matrix = tfidf.fit_transform(df['description'])  # 將所有摘要轉換為 TF-IDF 矩陣
    feature_names = np.array(tfidf.get_feature_names_out())  # 獲取所有特徵詞列表


    # 提取關鍵字
    tqdm.pandas()  # 初始化 tqdm 的 Pandas 擴展來顯示進度條
    df['keywords'] = df['description'].progress_apply(  # 對每個摘要應用關鍵詞提取函數
        lambda x: extract_keywords_tfidf(tfidf.transform([x]), feature_names)  # 將摘要轉換為 TF-IDF，提取關鍵詞
    )

    # df['keywords'] = [
    #     extract_keywords_tfidf(tfidf_matrix[i], feature_names)
    #     for i in tqdm(range(tfidf_matrix.shape[0]))
    # ]


    # 將關鍵字列表轉換為字符串
    df['keywords'] = df['keywords'].apply(lambda x: ','.join(x))

    print(df['keywords'])
    # return

    # 檢查是否存在 'keywords' 列，如果不存在則創建
    # cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'keywords'")
    query = f"""
        SELECT name 
        FROM pragma_table_info('{table_name}')
        WHERE name = ?
    """
    cursor.execute(query, ('keywords',))
    result = cursor.fetchone()
    if not result:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN keywords TEXT")
    

    # 更新數據庫中的 'keywords' 列
    update_query = f"UPDATE {table_name} SET keywords = ? WHERE show_id = ?"
    for _, row in tqdm(df.iterrows(), total=len(df)):
        cursor.execute(update_query, (row['keywords'], row['show_id']))


    # 提交更改並關閉連接
    connection.commit()
    cursor.close()
    connection.close()

    print(f"處理完成。共更新了 {len(df)} 條記錄。")


# 使用示例
# process_movie_summaries('localhost', 'username', 'password', 'movie_database', 'movie_summaries')



def main():
    load_dotenv()
    process_movie_summaries()

if __name__ == "__main__":
    main()