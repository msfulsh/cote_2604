'''
6번 문제
정수 배열 A가 주어진다.
배열에서 연속한 구간 하나를 골라 그 합이 가장 큰 값을 구하라.
예:
A = [3, 2, -6, 4, 0]
가능한 연속 구간 중 최대 합은 5 ([3,2])
A[0] 최대 3
A[1] 3+2,2
A[2] 5-6,-6
A[3] -1+4,+4
A[4] 4+0,0

어떤 레슨 감각인지
시간복잡도 목표
핵심 아이디어
'''
def solution(A):
    N = len(A)
    best = A[0]
    cur = A[0]
    for i in range(1,N):
        print(i,cur+A[i],A[i])
        cur = max(cur+A[i],A[i])
        best = max(best,cur)
        print(i,cur,best)
    return best

A=[3, 2, -6, 4, 0]
print(solution(A))
        