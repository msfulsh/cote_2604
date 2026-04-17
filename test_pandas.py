# import pandas as pd

# # 예시 평점 데이터 생성
# df = pd.DataFrame({
#     "user":   ["u1", "u1", "u2", "u2", "u3", "u3", "u4"],
#     "item":   ["A",  "B",  "A",  "C",  "B",  "C",  "D"],
#     "rating": [5,    3,    4,    2,    4,    5,    5]
# })

# # 원본 데이터 확인
# print("=== 원본 데이터 ===")
# print(df)
# print()

# # item 기준으로 rating 컬럼의 개수(count), 평균(mean) 계산
# item_stats = df.groupby("item")["rating"].agg(["count", "mean"]).reset_index()

# # 계산된 통계 확인
# print("=== 아이템별 평점 개수/평균 ===")
# print(item_stats)
# print()

# # 평균 평점이 높은 순으로 정렬
# item_stats = item_stats.sort_values(by="mean", ascending=False)

# # 정렬 결과 확인
# print("=== 평균 평점 높은 순 정렬 ===")
# print(item_stats)
# print()

# # user를 행(index), item을 열(columns), rating을 값(values)으로 하는 표 생성
# matrix = df.pivot_table(index="user", columns="item", values="rating")

# # 사용자-아이템 매트릭스 확인
# print("=== 사용자-아이템 매트릭스 ===")
# print(matrix)
# print()

# # 추천 대상 사용자 지정
# target_user = "u1"

# # 전체 item 목록 구하기
# all_items = set(df["item"])

# # target_user가 이미 본 item 목록 구하기
# seen_items = set(df[df["user"] == target_user]["item"])

# # 전체 item - 본 item = 아직 안 본 item
# not_seen_items = all_items - seen_items

# # 안 본 item 확인
# print(f"=== {target_user}가 안 본 아이템 ===")
# print(not_seen_items)
# print()

# # item_stats에서 안 본 item만 남기기
# recommend = item_stats[item_stats["item"].isin(not_seen_items)]

# # 평균 평점 높은 순으로 다시 정렬
# recommend = recommend.sort_values(by="mean", ascending=False)

# # 최종 추천 결과 확인
# print(f"=== {target_user} 추천 결과 ===")
# print(recommend)
# print()

# # 원본 df에 item별 count, mean 정보를 붙이기 위해 merge 수행
# merged = pd.merge(df, item_stats, on="item")

# # merge 결과 확인
# print("=== 원본 데이터 + 아이템 통계 merge ===")
# print(merged)
# print()

# # 간단한 가중 점수 생성: 평균 * 개수
# item_stats["score"] = item_stats["mean"] * item_stats["count"]

# # score 높은 순 정렬
# item_stats = item_stats.sort_values(by="score", ascending=False)

# # 가중 점수 결과 확인
# print("=== 가중 점수 기준 정렬 ===")
# print(item_stats)