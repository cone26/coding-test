# TGN
n = int(input())
for _ in range(n):
    current, future, adv = list(map(int, input().split()))
    if (future - adv) > current : print('advertise')
    elif (future - adv) < current :print('do not advertise')
    else : print('does not matter')