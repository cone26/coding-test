# 윷놀이
for _ in range(3):
    command = list(map(int,input().split()))
    if command.count(0) == 1 and command.count(1) == 3 : print('A')
    elif command.count(0) == 2 and command.count(1) == 2 : print('B')
    elif command.count(0) == 3 and command.count(1) == 1 : print('C')
    elif command.count(0) == 4 : print('D')
    elif command.count(1) == 4 : print('E')