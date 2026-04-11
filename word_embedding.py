'''
문제: Word Embedding Similarity Search

단어와 그에 대응하는 임베딩 벡터가 주어진다.
특정 기준 단어 target_word 와 가장 유사한 단어들을 찾아라.

단어 간 유사도는 코사인 유사도(cosine similarity) 로 계산한다.

단, 아래 조건을 만족해야 한다.

target_word 자신은 결과에서 제외한다.
exclude_words 에 포함된 단어들도 결과에서 제외한다.
코사인 유사도가 높은 순으로 정렬한다.
유사도가 같다면 사전순(alphabetical order) 으로 정렬한다.
결과는 상위 top_n 개의 단어를 리스트로 반환한다.
어떤 벡터의 norm이 0이면, 그 벡터와의 유사도는 0으로 처리한다.
'''
import numpy as np 
def cosine_similarity(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0
    
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def word_similarity(embeddings,target_word,exclude_words,top_n):
    target_word_vec = embeddings[target_word]
    score_list=[]
    for word,vec in embeddings.items():
        if word == target_word:
            continue
        if word in exclude_words:
            continue
        score = cosine_similarity(vec,target_word_vec)
        score_list.append((word,score))
        score_list.sort(key=lambda x: (-x[1], x[0]))
    return [item[0] for item in score_list[:top_n]]

embeddings = {
    "king":   [0.8, 0.7, 0.2],
    "queen":  [0.79, 0.69, 0.21],
    "man":    [0.7, 0.6, 0.1],
    "woman":  [0.69, 0.59, 0.11],
    "apple":  [0.1, 0.2, 0.9],
    "orange": [0.12, 0.18, 0.88]
}

target_word = "king"
exclude_words = ["man"]
top_n = 2

ans = word_similarity(embeddings,target_word,exclude_words,top_n)
print(ans)