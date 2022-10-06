# 다리 놓기
import math
# math.comb를 사용하면 바로 조합의 수를 알려줌
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    count = 0
    N,M = map(int,sys.stdin.readline().split())
    print(math.comb(M,N))