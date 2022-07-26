# 0 = not cute / 1 = cute
n = int(input())
score = []
for _ in range(n): score.append(int(input()))
if score.count(0) > score.count(1) : print('Junhee is not cute!')
else : print('Junhee is cute!')