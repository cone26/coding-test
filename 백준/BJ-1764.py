# 듣보잡
n,m = map(int,input().split())
listen = set([])
see = set([])
for _ in range(n): listen.add(input())
for _ in range(m): see.add(input())
answer = sorted(listen & see)

print(len(answer))
for i in answer: print(i)