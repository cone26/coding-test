# 덩치
n = int(input())
people = []
answer = []
for _ in range(n):people.append(list(map(int,input().split())))
for i in range(len(people)):
    count = 1
    for j in range(len(people)):
        if i == j : continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]: count += 1
    answer.append(count)

for i in answer : print(i,end=' ')