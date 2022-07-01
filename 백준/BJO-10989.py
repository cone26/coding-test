# 수 정렬하기 3
import sys
n = int(sys.stdin.readline())

arr = [0]*10001
for _ in range(n):
    num = int(sys.stdin.readline()) 
    arr[num] = arr[num] + 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)

# append 쓰니까 메모리 초과 떴는데 이거 왜 이러는지.. 공부해보기