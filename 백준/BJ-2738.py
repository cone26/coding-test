N,M = map(int,input().split())
a_list, b_list = [],[]
for _ in range(N):
    a_list.append(list(map(int,input().split())))
    

for _ in range(N):
    b_list.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        print(a_list[i][j]+b_list[i][j],end=' ')
    print()
