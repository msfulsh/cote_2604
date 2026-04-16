def solution(A):
    start = []
    end = []
    for i in range(len(A)):
        start.append(i-A[i])
        end.append(i+A[i])  
    start.sort()
    end.sort()    
    active = 0
    intersect = 0
    end_idx = 0 
    for s in starts:

        # 현재 시작점 s보다 먼저 끝난 원판들은
        # 지금 원판과 절대 만날 수 없으므로 active에서 제거
        while end_idx < N and ends[end_idx] < s:
            active -= 1
            end_idx += 1

        # while이 끝난 뒤 active는
        # "지금 시점(s)에 아직 살아 있는 이전 원판 수"
        # 따라서 현재 원판은 그 active개와 모두 교차
        intersect += active

        # 교차 개수가 1000만 초과면 -1
        if intersections > 10_000_000:
            return -1

        # 이제 현재 원판도 시작했으므로 active에 포함
        active += 1

    pass

'''
[-5, -4, 1, 2]
[-1, 0, 3, 5]

i=0
i=1
i=2 -> -1,0


'''