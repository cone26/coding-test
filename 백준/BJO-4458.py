import sys
n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().strip()
    print(line[0].upper()+ line[1:]) 