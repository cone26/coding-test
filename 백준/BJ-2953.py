# 나는 요리사다
score = 0
num = 0
for i in range(5):
    lst = list(map(int,input().split()))
    if sum(lst) > score : 
        score = sum(lst)
        num = i + 1
print(num, score)