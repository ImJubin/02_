## 입력값 받아서 정수화
#초기값 세팅

# 함수화 해버림. r.c위치치에 있는 파리 개수는

#M은 i j 만큼 증가

#n,m쓰기좋게만들어줌
#답이 잘못나올경우대비해서-1함
#N번 반복할 때 파리 개수

# M 안에서 (N-M+1) i j 행렬 돈ek

# 임시값 = 아까 캐치플라이함수
# 돌면서 최댓값 갱신


T = int(input())
M, N = 0

def catch_flies (flies, r, c):
    catch_sum = 0
    for i in range(N):
        for j in range(N):
            catch_sum += [r+i][c+j]
      
    return catch_sum

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    flies = list(map(int, input().split()) for _ in range(N))
    answers = -1

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = catch_flies(flies, i, j)
            if temp_sum < answers:
                temp_sum = answers
            
                
    

    print(f'#{tc} {answers}')