T = int(input()) # 입력값 받아서 정수화
N, M = 0, 0     # 초기값 세팅

def catch_fly(flies, r, c): # 함수화 해버림. r.c위치치에 있는 파리 개수는
    catch_sum = 0           # 
    for i in range(M):      
        for j in range(M):
            catch_sum += flies[r+i][c+j]       # M은 i j 만큼 증가

    return catch_sum

for tc in range(1, T+1):                        
    N, M = list(map(int, input().split()))      # n,m쓰기좋게만들어줌
    answer = -1                               # 답이 잘못나올경우대비해서-1함
    flies = [list(map(int, input().split())) for _ in range(N)] #N번 반복할 때 파리 개수

    for i in range(N-M+1):                      # M 안에서 (N-M+1) i j 행렬 돈다
        for j in range(N-M+1):
            temp_sum = catch_fly(flies, i, j)   # 임시값 = 아까 캐치플라이함수
            if answer < temp_sum:               # 돌면서 최댓값 갱신
                answer = temp_sum

    print(f'#{tc} {answer}')

# 파리채
# N 값과 M값을 받아야함 (쓰기 편하게 리스트화)
# 배열을 받는다
# M배열의 최댓값을 for문을 돌면서 더해줌
# max값비교

