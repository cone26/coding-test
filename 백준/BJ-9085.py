# 더하기
N = int(input())
for _ in range(N):
    M = int(input())
    lst = list(map(int,input().split()))
    print(sum(lst))