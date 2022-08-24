# 수 뒤집기
n = int(input())
for _ in range(n):
    m = input()
    sum = int(m) + int(m[::-1])
    print('YES') if sum == int(str(sum)[::-1]) else print('NO')