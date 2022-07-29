# 수 정렬하기2
import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
sorted_lst = sorted(lst)
for i in sorted_lst: print(i)