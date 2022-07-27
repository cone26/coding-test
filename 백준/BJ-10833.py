# 사과
n = int(input())
sum = 0
for _ in range(n):
    students, apples = list(map(int,input().split()))
    sum += apples % students
print(sum)