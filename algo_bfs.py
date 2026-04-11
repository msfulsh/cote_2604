'''
아이디어 bfs 이중for문
시간복잡도 O(V+E)=O(5V)=O(5nm)
변수 n,m = int[], board = int[][], chk = bool[][]
'''
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list (map(int,input().split()) ) for _ in range(n)]
chk = [[False]*m for _ in range(n)]
count = 0 
maxv=0
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x):
    rs = 1
    q = deque()
    q.append((y,x))
    while(q):
        ey,ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if board[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs +=1
                    q.append((ny,nx))
    return rs



for j in range(n) :
    for i in range(m):
        if board[j][i] == 1 and chk[j][i]== False:
            chk[j][i] = True
            count += 1
            maxv = max(bfs(j,i),maxv)

print(count)
print(maxv)