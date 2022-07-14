# 세 수
import sys
n = list(map(int, sys.stdin.readline().strip().split()))
n.remove(max(n)) ; n.remove(min(n));
print(n[0])

