'''
3번 문제
정수 배열 A가 주어진다.
배열에서 서로 다른 두 원소를 골라 합이 0이 되는 쌍이 하나라도 존재하면 1, 없으면 0을 리턴하라.
예시
A = [3, 1, -2, 5, 2]
-2 + 2 = 0 이므로 정답은 1
A = [1, 2, 3, 4]
합이 0 되는 쌍 없음 → 정답 0
조건
N은 최대 100,000
이번에도 3개만 답해줘:
어떤 레슨 감각인지 sort 후 투포인터
시간복잡도 목표 O(N*logN)
핵심 아이디어 sort후 왼쪽 오른쪽 합친것이 0이면 1리턴 탈출, 음수이면 왼쪽+1, 양수이면 오른쪽 +1 왼쪽<오른쪾 와일문
'''
def solution(A):
    N = len(A)
    A.sort()
    left = 0 
    right = N-1

    while left < right:
        s = A[left] + A[right]
        print(left,right,s)
        if s == 0:
            return 1
        elif s < 0:
            left += 1
        else :
            right -= 1
    if left == right:
        return 0
    pass
#A = [1, 2, 3, 4]
A = [3, 1, -2, 5, 2]
print(solution(A))