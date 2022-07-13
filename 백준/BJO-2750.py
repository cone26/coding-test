# 수 정렬하기
import sys
n = int(sys.stdin.readline().strip())

numArr = []
for _ in range(n): numArr.append(int(sys.stdin.readline().strip()))
numArr.sort()
for i in numArr: print(i)