# 킹,퀸,룩,비숍,나이트,폰
lst = list(map(int,input().split()))
piece = [1,1,2,2,2,8]
for i in range(len(lst)):print(piece[i]-lst[i],end=' ')