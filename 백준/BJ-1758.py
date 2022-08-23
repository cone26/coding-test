# 알바생 강호
n = int(input())
lst = []
sum = 0
for _ in range(n):lst.append(int(input()))
lst.sort(reverse=True)
for i in range(len(lst)):
    if lst[i] - i > 0 : sum += lst[i] - i
print(sum)