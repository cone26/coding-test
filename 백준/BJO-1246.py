# 모음의 개수
import sys
filter = ['a','e','i','o','u','A','E','I','O','U']
while True :
    sentence = sys.stdin.readline().strip()
    sum = 0
    for i in sentence :
        if i in filter : sum += 1
    if sentence == '#': break
    print(sum)