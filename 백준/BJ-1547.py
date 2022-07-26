# 공
n = int(input())
ball = 1
for _ in range(n):
    position = list(map(int, input().split()))
    if position[0] == ball : ball = position[1]
    elif position[1] == ball : ball = position[0]
print(ball)