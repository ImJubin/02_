T = 10

# 0: 상, 1:좌, 2: 우

dr = [-1, 0, 0]
dc = [0, -1, 1]
# 현재 위 일 땐 좌>우>상 순으로 탐색해라
search_dir = [[1,2,0], [0,1], [0,2]]

for _ in range(1, T+1):
    dir = 0
    r = 99
    c = -1

    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    c = ladder[99].index(2)

    while r > 0:
        # 어디로 이동할건데?
        
        for i in range(len(search_dir[dir])):
            next_dir = search_dir[dir][i]
            next_r = r+dr[next_dir]
            next_c = c+dc[next_dir]
            
            # print(next_r, next_c)
            #인덱스 이내
            if 0 <= next_r and 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break
        # print(r, c)

    print(f'#{tc} {c}')