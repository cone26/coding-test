# 홀수일까 짝수일까
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num % 2 == 0 : print('even')
    else : print('odd')