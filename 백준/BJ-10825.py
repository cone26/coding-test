# 국영수
import sys
N = int(sys.stdin.readline())
students = [list(sys.stdin.readline().split()) for _ in range(N)]
students.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in students:print(i[0])