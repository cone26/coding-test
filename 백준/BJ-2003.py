# 집합
import sys
n = int(sys.stdin.readline())
S=set()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'add': S.add(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) not in S:continue
        S.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in S:print(1)
        else : print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S: S.remove(int(command[1]))
        else : S.add(int(command[1]))
    elif command[0] == 'all': S = set([x for x in range(1,21)])
    else : S = set()