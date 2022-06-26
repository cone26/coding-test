# 덱 - 뼈대문제

import sys

n = int(sys.stdin.readline())
dequeue = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        dequeue.insert(0,command[1])
    elif command[0] == 'push_back':
        dequeue.append(command[1])
    elif command[0] == 'pop_front':
        if len(dequeue) == 0 : print(-1)
        else : print(dequeue.pop(0))
    elif command[0] == 'pop_back':
        if len(dequeue) == 0 : print(-1)
        else : print(dequeue.pop())
    elif command[0] == 'size':
        print(len(dequeue))
    elif command[0] == 'empty':
        if len(dequeue) == 0 : print(1)
        else : print(0)
    elif command[0] == 'front':
        if len(dequeue) == 0 : print(-1)
        else : print(dequeue[0])
    else:
        if len(dequeue) == 0 : print(-1)
        else : print(dequeue[-1])