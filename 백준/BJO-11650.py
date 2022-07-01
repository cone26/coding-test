#좌표 정렬

import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    [a,b] = map(int, sys.stdin.readline().split())
    arr.append([a,b])
s_arr = sorted(arr)

for j in range(n):
    print(s_arr[j][0], s_arr[j][1])