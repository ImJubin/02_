from collections import deque

# N+1 * ... 인덱스처리 1 부터 
N, M, V = map(int, input().split())
adj_matrix
visited = [0]*(N+1) #N까지쓰도록
#v : 현재 방문 지점, 계속 바뀌어  v 로구분
def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1, N+1):
        #ㄱ. i 지점을 방문하지 않았고
        #ㄴ. v(현지점)와 i(다음 지점)이 연결 상태인 경우
        # 1 2 4 ....
        if not visited[i] and adj_matrix[v][i] ==1:
            dfs(i)


#인접행렬 입력받아 저장 끝
for i in range():
    a, b = map
    adj_matrix[a][b] = 1
    adj_matrix[b][a]



def bfs(v):
    q = deque()

    print(v, end=" ")
    visited[v] = 2
    q.append(v)
    
    while q:
        cur_pos = q.popleft
        for i in range(1, N+1):
            if not visited[i] == 1 and adj_matrix[cur_pos][i] == 1:
                print(i, end=" ")
                visited[i] = 2
                q.append(i)

    dfs(V)
    #방문배열초기화
    print()
    bfs(V)
