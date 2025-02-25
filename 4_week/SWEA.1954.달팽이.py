T = int(input())
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    
    numbers = [[0]*N for _ in range(N)]
    
    r = c = 0
    count = 1
    # 우측이 초기 방향
    dir = 0
    for i in range(N*N):
        # 1. 현재 지점에 count를 찍고
        numbers[r][c] = count

        # 2. 다음 지점 좌표를 찾아 이동
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 밖을 벗어나거나 이미 채워진 값은 이동하면 안 됨
        if nr < 0 or nr >= N or nc < 0 or nc >= N or numbers[nr][nc] != 0:
            dir = (dir+1)%4
            nr = r + dr[dir]
            nc = c + dc[dir]
        
        r = nr
        c = nc 
         
        # 3. count 증가
        count += 1

    for i in range(N):
        for j in range(N):
            print(numbers[i][j], end=" ")
        print()
