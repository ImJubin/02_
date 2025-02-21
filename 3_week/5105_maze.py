def bfs(i, j, N): #시작 위치 i j, 크기 N
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []      # 큐생성
    q.append([i,j])# 시작점 인큐
    visited[i][j] = 1# 시작점 인큐 표시
    # 탐색(큐에 남은 칸이 없을 때까지, 큐가 비워질 때까지)
    while q:
        ti, tj = q.pop(0)   # t <- 디큐
                            # t에서 할 일...

        if maze[ti][tj] == 3:   # visit(t) 어라? 출구네? >> return 1(==# 출구(3)에 도착하면 1 아님 0)
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 추가 (==# 입구에서 출구 사이의 빈칸 수)
        # (==t에 인접 w중, 인큐되지 않은 곳이면)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            # 미로를 벗어나지 않고, 벽이아니면,
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj]) # 인큐, 표시
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

# N = int(input())
# maze = [list(map(int, input())) for _ in range(N)]
# sti, stj = find_start(N)
# ans = bfs(sti, stj, N)
# print(ans)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    #미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N) # 이중 포문 빠져나오는 거 간단하게 구현하기

    ans = bfs(stj, stj, N)
    print(f'#{tc} {ans}'

    #cf. 강의 버전은 str으로 구현되어 해당코드와 약간 다름