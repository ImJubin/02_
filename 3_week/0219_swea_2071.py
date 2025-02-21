T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    sum = 0
    for num in arr:
        sum += num
        
    
    print(f'#{tc} {round(sum/len(arr))}')