# 단어 뒤집기
n = int(input())
for _ in range(n):
    phrase = list(input().split())
    for i in phrase: print(i[::-1],end = ' ')