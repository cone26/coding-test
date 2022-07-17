# 플러그
import sys
n = int(sys.stdin.readline().strip())
answer = 0
for _ in range(n):
    answer += int(sys.stdin.readline().strip())
print(answer-(n -1))