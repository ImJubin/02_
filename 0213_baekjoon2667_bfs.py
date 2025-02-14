n = int(input())            # 
arr = [list(map(int, input())) for _ in range(n)]
vili_cnt = 0
house_cnt = 0
h_cnt = []

def dfs(a, b):
    arr[a][b] = 0 #arr 점 초기값 세팅
    dr = [-1, 0, 1, 0] # 위 오 아 왼
    dc = [0, 1, 0, -1]
    global house_cnt 
    house_cnt += 1
    for k in range(4):  # k는 위 오 아 왼 시계 방향으로 탐색
        nr = a+dr[k]    # nr 기존 점인 (a,b)에서 상하 이동
        nc = b+dc[k]    # nc 기존점인 (a,b)에서 좌우이동
        if nr < 0 or nc<0 or nr>n-1 or nc>n-1: # 다음 방향 탐색이 범위 바깥에 있다면? 
              continue
        if arr[nr][nc] == 1: # (다음 방향 지점이 1로 연결되어있다면 0으로 바꿔준다.)
            arr[nr][nc] = 0 
            dfs(nr, nc)

for i in range(n):      
    for j in range(n):      # i j 방향으로 돌때 ij방향이 1일 때, 단지 수도 카운트 해준다.
        if arr[i][j] == 1:
            dfs(i, j)           
            vili_cnt += 1               
            h_cnt.append(house_cnt)     #[각 단지내 집에 수에 집의 수 인자를 추가한다]
            house_cnt = 0           

h_cnt.sort()                            #오름차순 정의

print(vili_cnt)