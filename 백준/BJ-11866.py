# 요세푸스 문제
import sys
from collections import deque 
n,k = list(map(int,sys.stdin.readline().split()))
people = [x for x in range(1,n+1)]
people = deque(people)
answer = deque()
print('<',end='')
while people :
    for i in range(k-1): people.append(people.popleft())
    print(people.popleft(),end='')
    if people: print(', ',end='')
print('>')