# 뜨거운 붕어빵
import sys
n = int(sys.stdin.readline().split()[0])
for _ in range(n):
    str = sys.stdin.readline().strip()
    print(str[::-1])