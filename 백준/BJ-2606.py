# 바이러스
n = int(input())
m = int(input())
graph = {}
for i in range(1,n+1):graph[i] = []
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(graph,start,visited=set()):
    if start not in visited:
        visited.add(start)
        nbr = set(graph[start])-visited
        for v in nbr : dfs(graph,v,visited)
    return visited
result = dfs(graph,1)
print(len(result)-1)