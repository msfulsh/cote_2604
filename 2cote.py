'''
2번 문제 정수 배열 A가 주어진다.
배열에서 어떤 인덱스 P를 기준으로 왼쪽 부분과 오른쪽 부분으로 나눈다.
왼쪽 부분 합 = A[0] + A[1] + ... + A[P]
오른쪽 부분 합 = A[P+1] + ... + A[N-1]
이때 왼쪽 부분 합과 오른쪽 부분 합이 같은 분할의 개수를 구하라.
예시
A = [2, -2, 2, -2, 2, -2]
가능한 split:
P=0 → 왼쪽 2, 오른쪽 -2 → X
P=1 → 왼쪽 0, 오른쪽 0 → O
P=2 → 왼쪽 2, 오른쪽 -2 → X
P=3 → 왼쪽 0, 오른쪽 0 → O
P=4 → 왼쪽 2, 오른쪽 -2 → X
정답은 2
조건
N은 2 이상 100,000 이하
이번에도 답은 3개만:
어떤 레슨 감각인지 sumleft, sumright 합계가 같을때 count+1  포문반복
시간복잡도 목표 O(N)
핵심 아이디어
'''
def solution(A):
    N = len(A)
    sumleft = A[0]
    sumright = sum(A) - A[0]
    if sumleft == sumright :
        count = 1
    else : 
        count = 0

    for i in range(1,N-1):
        sumleft += A[i]
        sumright -= A[i]
        if sumleft == sumright:
            count += 1
        print (i,sumleft,sumright,count)
    return count

A = [2, -2, 2, -2, 2, -2]
print(solution(A))