# 민균이의 비밀번호
n = int(input())
lst = []
for _ in range(n):lst.append(input())
answer = lst[0]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i])[::-1] == lst[j] : answer = lst[j]
print(len(answer),answer[len(answer)//2])