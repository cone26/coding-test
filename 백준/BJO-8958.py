# ox퀴즈

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    oTotal = 0; total = 0
    command = sys.stdin.readline()
    for i in command:
        if i == 'O': 
            oTotal = oTotal + 1
            total = total + oTotal
        elif i == 'X': oTotal = 0
    print(total)