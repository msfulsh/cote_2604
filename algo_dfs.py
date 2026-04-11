'''
아이디어 이중for문 dfs재귀
시간복잡도
'''
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]
result = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    rs = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N:
            if board[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                rs += dfs(ny,nx)
    return rs



for j in range(N):
    for i in range(N):
        if board[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            result.append(dfs(j,i))

print(len(result))
result.sort()
for i in result:
    print(i)
