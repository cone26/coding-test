# 점수계산
n = int(input())
score = 0; sum = 0
scores = list(map(int, input().split()))
for i in scores:
    score = score + 1 if i == 1 else 0
    sum += score
print(sum)