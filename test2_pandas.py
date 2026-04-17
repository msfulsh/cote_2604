df = pd.DataFrame({
    "user":   ["u1", "u1", "u2", "u2", "u3", "u3", "u4"],
    "item":   ["A",  "B",  "A",  "C",  "B",  "C",  "D"],
    "rating": [5,    3,    4,    2,    4,    5,    5]
})


# 1. item별로 rating의 count, mean 구하기
df.groupby("item")["rating"].agg(["count", "mean"]).rest_index()
# 힌트: 그룹으로 묶기 / 여러 집계함수 적용 / 인덱스 되돌리기
df.groupby("item")["rating"].agg(["count", "mean"]).rest_index()


df = pd.DataFrame({
    "user":   ["u1", "u1", "u2", "u2", "u3", "u3", "u4"],
    "item":   ["A",  "B",  "A",  "C",  "B",  "C",  "D"],
    "rating": [5,    3,    4,    2,    4,    5,    5]
})

item별로 rating의 count,mean구하기 인덱스는 초기화필요


df.groupby("item")["rating"].agg(["count","mean"]).reset_index()

df.sort_values(by="mean", ascending=False)
df.pivot_table(index="user",columns="item",values="rating")
    












# 2. mean 기준 내림차순 정렬
df.sort(by="mean", ascending=False)
# 힌트: 정렬 함수 / 내림차순이면 False

# 3. user-item-rating 형태의 매트릭스 만들기
df.pivot_table(index="user", columns="item", values="rating")
# 힌트: 행/열/값으로 표 만들기

# 4. item 컬럼을 집합으로 만들기
set(df["item"])
# 힌트: 중복 제거 느낌, 파이썬 내장 함수

# 5. target_user가 본 item만 집합으로 만들기
set(df[df["user"] == target_user]["item"])
# 힌트: 먼저 user 필터링, 그다음 item만 뽑아서 집합화

# 6. not_seen_items 안에 있는 item만 필터링
df[df["item"].isin(not_seen_items)]
# 힌트: 컬럼 값이 특정 목록/집합 안에 포함되는지 검사