'''
7번 문제
정수 배열 A가 주어진다.
배열에서 서로 같은 값을 가지는 두 원소 A[P], A[Q] 를 고른다. (P < Q)
이때 두 원소 사이의 거리는: Q - P 이다.
배열 안에 존재하는 모든 같은 값 쌍들에 대해 거리를 계산했을 때,
그중 최솟값을 구하라. 같은 값을 가진 쌍이 하나도 없으면 -1을 리턴하라.
A = [5, 1, 3, 5, 2, 3]
같은 값 쌍:
값 5: 위치 0, 3 → 거리 3
값 3: 위치 2, 5 → 거리 3
정답:
3
아이디어 : for문을 돌리고 A[i]를 딕셔너리에 저장, 기존에 저장된게 있으면 거리를 저장 그리고 min을 갱신
시간복잡도 : O(N)
'''
def solution(A):
    N = len(A)
    chk = {}
    min_dist = float('inf')
    for i in range(N):
        if A[i] in chk:
            dist = i-chk[A[i]]
            min_dist = min(dist,min_dist)
        chk[A[i]] = i
    if min_dist =- float('inf'):
        return -1
    return min_dist
    