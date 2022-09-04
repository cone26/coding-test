# 점수 집계
N = int(input())
for _ in range(N):
    scores = list(map(int,input().split()))
    scores.sort()
    scores.pop(0)
    scores.pop(-1)
    print('KIN') if max(scores) - min(scores) >= 4 else print(sum(scores))