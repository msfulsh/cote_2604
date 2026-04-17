'''
1번 문제
정수 배열 A가 주어진다. 인덱스 P로 배열을 두 부분으로 나누려고 한다.
왼쪽 부분: A[0] ~ A[P] 오른쪽 부분: A[P+1] ~ A[N-1]
이때 좋은 분할(good split) 이란, 
왼쪽 부분에 존재하는 서로 다른 값의 개수 오른쪽 부분에 존재하는 서로 다른 값의 개수 가 서로 같은 경우를 말한다.
좋은 분할의 개수를 구하라.
A = [1, 2, 1, 2, 3]
가능한 분할:
P=0 → 왼쪽 {1} = 1개, 오른쪽 {1,2,3} = 3개 → X
P=1 → 왼쪽 {1,2} = 2개, 오른쪽 {1,2,3} = 3개 → X
P=2 → 왼쪽 {1,2} = 2개, 오른쪽 {2,3} = 2개 → O
P=3 → 왼쪽 {1,2} = 2개, 오른쪽 {3} = 1개 → X
정답은 1
예시 2
A = [1, 1, 1, 1]
P=0 → 왼쪽 {1}=1, 오른쪽 {1}=1 → O
P=1 → 왼쪽 {1}=1, 오른쪽 {1}=1 → O
P=2 → 왼쪽 {1}=1, 오른쪽 {1}=1 → O
정답은 3
조건
N은 1 이상 100,000 이하
배열 원소는 정수
어떤 레슨 감각으로 풀 건지 왼쪽 오른쪽 각각 딕셔너리를 관리. 딕셔너리 count도 별도로 관리 포문돌면서 왼쪽에서 A[i] 더하고 오른쪽에서 A[i]빼고 양쪽 count 같다면 전체 count +1
시간복잡도 목표
핵심 아이디어 2~3줄
'''
def solution(A):
    N = len(A)
    left={}
    right={}
    for i in range(N):
        x = A[i]
        if x in right:
            right[x] +=1
        else :
            right[x] =1
    rightcount=len(right)
    print(right,rightcount)

    leftcount=0
    count = 0

    for i in range(N-1):
        x = A[i]
        if x in left:
            left[x] +=1
        else :
            left[x] =1
            leftcount += 1
        right[x] -= 1
        if right[x] == 0 :
            rightcount -=1
        if leftcount == rightcount:
            count+=1
    return count

#A = [1, 2, 1, 2, 3]
A = [1, 1, 1, 1]
print(solution(A))