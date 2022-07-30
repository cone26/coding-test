# 오타맨 고창영
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    num,word = sys.stdin.readline().split()
    num = int(num); word = list(word)
    word.pop(num-1)
    print(''.join(word))
