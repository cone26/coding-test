# 배열 합치기
n,m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
for i in range(m) : lst1.append(lst2[i])
lst1 = map(str,sorted(lst1))
print(' '.join(lst1))
