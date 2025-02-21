'''
N = 팀원 수, M = 명령 수
flg_list = 배열
a, b, c = 난이도, 기준, 간격
인덱스 땡겨야 하기 때문에 b-1

N에
'''


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag_list = list(map(int, input().split()))

    for _ in range(M):
        a, b, c = map(int, input().split())

        for i in range(b-1, b+c-1):
            if i>= N:
                break

            flag_list[i] = (flag_list[i]+1) % 2

    print(f'#{tc}', *flag_list)
