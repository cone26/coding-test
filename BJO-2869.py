# 달팽이는 올라가고 싶다
import sys


a,b,v = map(int,sys.stdin.readline().split())
day = (v - b)/(a - b)
print(int(day) if day == int(day) else int(day)+1)


# 시간초과 코드
# while m < v:
#     m += a
#     if m != v and m < v: m -= b
#     day = day+1
# print(day)
