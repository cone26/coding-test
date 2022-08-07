# 요세푸스 문제
from collections import deque
n, k = list(map(int,input().split()))
people =deque([x for x in range(1,n+1)])
dead_list = []

while len(people) > 0 :
    for j in range(k-1): people.append(people.popleft())
    dead_list.append(str(people.popleft()))
print('<',end='')
print(', '.join(dead_list),end='')
print('>')