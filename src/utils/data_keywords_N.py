import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tqdm import tqdm
import os
from dotenv import load_dotenv




# 定義一個函數來從文本中提取 TF-IDF 關鍵詞
def extract_keywords_tfidf(text, tfidf_matrix, feature_names, num_keywords=5):
    doc_index = tfidf_matrix.getrow(-1)  # 取出最新一行（即當前文本）的 TF-IDF 向量
    doc_weights = doc_index.toarray().flatten()  # 將稀疏矩陣轉換為一維數組
    top_indices = doc_weights.argsort()[-num_keywords:][::-1]  # 按權重排序，選出前 num_keywords 個最高值
    return [feature_names[i] for i in top_indices]  # 返回對應的關鍵詞列表



# 定義一個處理電影摘要的函數
def process_movie_summaries(host=None, user=None, password=None, database=None,name='N'):
    # 連接到MySQL數據庫
    connection = mysql.connector.connect(
        host = host or os.getenv(f'MYSQL_HOST_{name}'),
        user = user or os.getenv(f'MYSQL_USER_{name}'),
        password = password or os.getenv(f'MYSQL_PASSWORD_{name}'),
        database = database or os.getenv(f'MYSQL_DATABASE_{name}')
    )
    cursor = connection.cursor()

    print(cursor)
    return




    # 讀取電影摘要
    query = f"SELECT id, summary FROM {table_name}"
    df = pd.read_sql(query, connection)

    # 初始化TF-IDF向量器
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)

    # 擬合TF-IDF向量器並轉換文本
    tfidf_matrix = tfidf.fit_transform(df['summary'])
    feature_names = np.array(tfidf.get_feature_names_out())

    # 提取關鍵字
    tqdm.pandas()
    df['keywords'] = df['summary'].progress_apply(
        lambda x: extract_keywords_tfidf(x, tfidf.transform([x]), feature_names)
    )

    # 將關鍵字列表轉換為字符串
    df['keywords'] = df['keywords'].apply(lambda x: ','.join(x))

    # 檢查是否存在 'Keywords' 列，如果不存在則創建
    cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'Keywords'")
    result = cursor.fetchone()
    if not result:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN Keywords TEXT")

    # 更新數據庫中的 'Keywords' 列
    update_query = f"UPDATE {table_name} SET Keywords = %s WHERE id = %s"
    for _, row in tqdm(df.iterrows(), total=len(df)):
        cursor.execute(update_query, (row['keywords'], row['id']))

    # 提交更改並關閉連接
    connection.commit()
    cursor.close()
    connection.close()

    print(f"處理完成。共更新了 {len(df)} 條記錄。")

# 使用示例
# process_movie_summaries('localhost', 'username', 'password', 'movie_database', 'movie_summaries')



def main():
    # extract_keywords_tfidf()
    load_dotenv()
    process_movie_summaries()

if __name__ == "__main__":
    main()