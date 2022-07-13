# 10부제
import sys
n = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().split())
count = 0
for i in nums : 
    if n == i : count += 1
print(count)