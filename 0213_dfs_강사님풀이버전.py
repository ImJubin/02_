# 필요 변수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
graph = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
cnts = []

def dfs(r,c):
    global cnt

    cnt += 1
    visited[r][c] = 1


    for dir in range(len(dr)):
        nr = r+df[dir]
        nc = c+dc[dir]
        #방문가능하니?>>> 언제불가능?
        #ㄱ.범위 안 쪽 >> 밖 또는 연결 x 또는 방문했음 
        #ㄴ.연결 되어 있음  >>일때 컨티뉴
        #ㄷ.방문 안 했음
        if 0 > nr or nr >= n or 0 > nc or nc >= N: 
            continue
        if  graph[nr][nc] == "0" or visited[nr][nc] == 1:
            continue
        #정수보다 객체비교가 더 느림. 

for i in range(N):
    for j in range(N):
        
        if graph[i][j] == "1" or visited == 1:
            continue

        cnt = 0

        dfs(i,j)
        cnts.append(cnt)

        