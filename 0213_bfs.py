from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
vili_cnt = 0
house_cnt = 0
h_cnt = []

# def dfs(a, b):
#     arr[a][b] = 0
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     global house_cnt 
#     house_cnt += 1
#     for k in range(4): 
#         nr = a+dr[k]
#         nc = b+dc[k]
#         if nr < 0 or nc < 0 or nr > n-1 or nc > n-1:
#             continue
#         if arr[nr][nc] == 1: 
#             arr[nr][nc] = 0
#             dfs(nr, nc)

def bfs(a,b):
    q = deque()
    global house_cnt 
    arr[a][b] = 0
    house_cnt += 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    q.append((a, b))

    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if nr < 0 or nc < 0 or nr > n-1 or nc > n-1:
                continue

            if arr[nr][nc] == 1: 
                q.append((nr, nc))
                arr[nr][nc] = 0
                house_cnt += 1


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            # dfs(i, j)
            bfs(i,j)
            vili_cnt += 1
            h_cnt.append(house_cnt)
            house_cnt = 0

h_cnt.sort()

print(vili_cnt)
for i in range(len(h_cnt)):
    print(h_cnt[i])