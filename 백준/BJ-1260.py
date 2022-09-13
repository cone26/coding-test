# dfs 와 bfs
from collections import defaultdict


N,M,V = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def recursive_dfs(v,discoverd = []):
    discoverd.append(v)
    for w in graph[v]:
        if w not in discoverd:
            discoverd = recursive_dfs(w)
    return discoverd

dfs = recursive_dfs(V)
print(*dfs)

def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    while queue :
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
    return discoverd

bfs = iterative_bfs(V)
print(*bfs)