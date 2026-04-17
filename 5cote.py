'''
5번 문제
정수 배열 A가 주어진다.
배열을 정렬한 뒤, 서로 인접한 두 수의 차이 중 최솟값을 구하라.
예시
A = [8, 1, 5, 3, 12]
정렬하면 [1, 3, 5, 8, 12]
인접 차이:
3-1 = 2
5-3 = 2
8-5 = 3
12-8 = 4
정답은 2
이번에도 3개만 답해줘:
어떤 레슨 감각인지 sort하고 뒤-앞을 변수에 넣고 min갱신
시간복잡도 목표 O(N)
핵심 아이디어 sort하고 뒤-앞을 변수에 넣고 min갱신
'''
def solution(A):
    A.sort()
    N = len(A)
    minv = float('inf')
    for i in range(N-1):
        print(minv,A[i+1]-A[i])
        minv = min(A[i+1]-A[i],minv)
    return minv
    pass

A=[8, 1, 5, 3, 12]
solution(A)