# 중복 뺴고 정렬하기
n = int(input())
lst = list(map(int,input().split()))
lst = list(set(lst))
lst.sort()
for i in lst : print(i, end=' ')