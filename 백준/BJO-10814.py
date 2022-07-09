# 나이 순 정렬
import sys
n = int(sys.stdin.readline())
member = []
for _ in range(n): 
    age,name = sys.stdin.readline().strip().split()
    age = int(age)
    member.append((age,name))
member.sort(key = lambda x:x[0])
for i in member : print(i[0],i[1])