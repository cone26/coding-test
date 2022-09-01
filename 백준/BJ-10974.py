# 순열
from itertools import permutations
N = int(input())
lst = [str(x+1) for x in range(N)]
for i in list(permutations(lst,N)): print(" ".join(i))