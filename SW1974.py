T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # 가로줄
    for i in range(9):
        if len(set(puzzle[i])) != 9:
            result = 0

    # 세로줄
    coloumn = {}
    for j in range(9):
        for i in range(9):
                coloumn.add(puzzle[i][j])
    if len(coloumn) != 9:

    # 3 * 3
    # for 

        print(f'#{tc} {result}')
