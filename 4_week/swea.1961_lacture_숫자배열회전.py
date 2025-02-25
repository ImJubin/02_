T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    #각각의 줄을 numbers에 넣어주기
    numbers = []
    for i in range(N):
        numbers.append(list(map(int, input().split())))
#3차원 배열 = 리스트 안에 이차원 배열들 저장
    turns = []

    for i in range(3):
        temp_arr = []
        for i in range(N):
            cur_row = []
            for j in range(N):
                cur_row.append(numbers[N-1-j][i])  #끝 인덱스에서 j만큼 뺌 / j위치와 i 위치를 바꿈
            temp_arr.append(cur_row) #바꾼 한줄한줄을 temp_arr에 저장장
        turns.append(temp_arr)

        numbers = temp_arr    

    print(f'#{tc}')

    for i in range(N):
        
        for j in range(3):
            print(' '.join(map(str, turns[j][i])), end=" ") #출력 양식 맞추기 위해 스트링으로 바꾸고 여백 없이. join사용
        print()


        #''.join(["1", "2", "3"])-->
        # "123"