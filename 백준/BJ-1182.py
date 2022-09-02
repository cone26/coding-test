# 부분순열의 합
from itertools import combinations
N,S = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
for i in range(N):
    for j in combinations(lst,i+1):
        if sum(list(j)) == S : count += 1
print(count)