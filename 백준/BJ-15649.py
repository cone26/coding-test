# N과M (1)
from itertools import permutations
N,M = map(int,input().split())
lst = [str(x+1) for x in range(N)]

for i in list(permutations(lst,M)) : print(" ".join(i))