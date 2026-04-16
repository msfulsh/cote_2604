def solution(A, B):
    N = len(A)

    # 선분이 없으면 0개
    if N == 0:
        return 0

    # 첫 번째 선분은 우선 선택
    count = 1
    last_end = B[0]

    # 두 번째 선분부터 확인
    for i in range(1, N):
        # 시작점이 마지막으로 고른 선분의 끝점보다 커야 안 겹침
        # 문제에서 끝점 포함이고, 한 점만 닿아도 겹친다고 했으므로 > 사용
        if A[i] > last_end:
            count += 1
            last_end = B[i]

    return count