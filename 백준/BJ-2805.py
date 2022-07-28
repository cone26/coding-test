# 나무 자르기
# 이분 탐색
import sys 
n, m = list(map(int,sys.stdin.readline().split()))
trees = list(map(int,sys.stdin.readline().split()))
# for i in reversed(range(max(trees)-1)):
#     sum = 0
#     for j in trees :
#         if (j - i) > 0 :  sum += (j - i)
#     if sum == m : 
#         print(i)
#         break
low,high = 1,max(trees)

while low <= high:
    sum = 0
    middle = (low + high) // 2
    for i in trees:
        if i >= middle : sum += (i - middle)
    if sum >= m : low = middle + 1
    else : high = middle - 1
print(high)