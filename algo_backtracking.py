import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []
chk[] = [False] * (N+1)


def recur(num):
    if num == M:
        print(' '.join*(map(str,rs)))
        return
    for i in range(1:N+1):
        if chk[i] == false:
            chk[i] = true 
            rs.append(i)
            recur(num+1)
            chk[i]
            rs.pop()

recur(0)

























import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []
chk = [False]*(N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1:N+1):
        if chk[i] == False:
            chk[i] = TRUE처리
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()

recur(0)






'''
1. 아이디어 순열 출력 재귀함수를 사용 
포문시작
숫자가 꽉차면 쌓인거 출력
숫자 확인해서 false일때만 아래 동작
확인한숫자 TRUE처리
숫자 확인 false일때 넣기 append
위함수 재귀호출
숫자가 false이라면 꺼내기
2. 시간복잡도 순열 8이하?
3. 변수
'''
