'''
1) 델타 [[0,1],[1,0],[0,-1],[-1,0]]
이렇게 세팅하면, 어떻게 꺼내써야할까?

델타[i][0]
델타[i][1]
이렇게 쓰면 된다.
0, 1, 2, 3 에서 [0,1]은 0번째값은 r, 1번째 값은 c를 가리키기 때문이다.

2) 그래서 델타 탐색 어떻게 한다고?
next_r = r + dr
next_c = r + dc

3) 먼저 빈 행렬을 세팅한 뒤 , 맞춰서 돌아준다.

4) 단축평가시 순서 주의해야 한다. 끝의 or 뒤 조건까지 왔으면, 그 앞의 것들은 다 해당되지 않았단 말이다.
i가 정해진 범위를 넘어가면 프로그램 에러가 나기 때문에, 같은 or 조건이라도 앞에 배치한다.
0이 아닌 값이란 의미는 이미 돌아줘서 +1씩 카운팅 되었단 뜻이므로 안돌아줘도 됨.
그래서 값 != 0 일때 조건도 추가.

5) 범위 바꾸기는
(i+1)%4 0 1 2 3 0 1 2 3 이렇게 오른쪽부터 시계방향으로 돌게 된다.

6) 초기값 세팅 중요
r = c = 0. 0,0부터 시작.
dir도 설정해주기. 오른쪽부터 시작하니깐 dir = 0

'''
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
