# 막대기
import sys
num = int(sys.stdin.readline())
sticks=[]
count = 1
for _ in range(num): sticks.append(int(sys.stdin.readline()))
top = sticks[-1]
for i in reversed(sticks):
    if i > top: 
        top = i
        count += 1
print(count)