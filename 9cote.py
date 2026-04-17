'''
9번 문제
정수 배열 A가 주어진다.
배열에서 어떤 두 인덱스 P < Q를 골라:
A[P] + A[Q]의 값이 K 이하가 되는 쌍이 몇 개인지 구하라.
예시
A = [1, 5, 2, 4, 3]
K = 6
가능한 쌍:
(1,2) → 1+2 = 3
(1,4) → 1+4 = 5
(1,3) → 1+3 = 4
(1,5) → 1+5 = 6
(2,3) → 2+3 = 5
(2,4) → 2+4 = 6
정답: 6
조건
N은 최대 100,000
모든 원소는 정수
아이디어 : 우선 sort를 하자 
[1,2,3,4,5] K=6
1,5 -> 1,2  1,3 1,4 만족 
2,5 X
2,4 -> 2,3 만족
3,4 X 
시간복잡도 O(N)

'''
def solution(A,K):
    A.sort()
    N = len(A)
    left = 0
    right = N-1
    count = 0

    while left < right:
        s = A[left] + A[right]
        if s<=K:
            count += right - left
            left +=1
        else :
            right -=1
    return count
    pass

