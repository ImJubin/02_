T = int(input())
N, M = 0, 0

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    answer = -1
    flies = [list(map(int, input().split())) for _ in range(N)]

    prefix_sum = [[0]*(n+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1 + N+10):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + prefix_sum[i][j-1] + prefix_sum[i-1][j-1]

    for i in range(M, N+1):
        for j in range(M, N+1):
            temp_sum = prefix_sum[i][j] - prefix_sum[i-M][j] - prefix_sum[i][j-M] + prefix_sum[i-M][j-M]
            if answer < temp_sum:
                answer = temp_sum
 

    print(f'#{tc} {answer}')

# 파리채
# N값과 M값을 받아야함 (쓰기 편하게 리스트화)
# 배열을 받는다 
# M배열의 최댓값을 for문을 돌면서 더해줌
# max값비교

