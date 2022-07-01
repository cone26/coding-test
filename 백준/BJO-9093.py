# 단어 뒤집기 => 다시
# 다시
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    reverse_str=''
    for c in line:
        reverse_str = c + reverse_str
    print(reverse_str)

        
