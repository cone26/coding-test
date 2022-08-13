# 평균은 넘겠지
num = int(input())
for _ in range(num):
    sum = 0
    command = list(map(int,input().split()))
    for i in range(1,command[0]+1): sum += command[i]
    average = sum / command[0]
    count = 0
    for j in range(1,command[0]+1) : 
        if command[j] > average: count += 1
    print(f'{count / command[0] * 100:.3f}%')
