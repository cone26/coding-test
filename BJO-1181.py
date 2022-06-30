# 단어 정렬

import sys

n = int(sys.stdin.readline())

words = []
for _ in range(n) :
    word = sys.stdin.readline().strip()
    if word not in words:
        words.append(word)
    

words.sort()
words.sort(key = lambda x : len(x))
for i in words: print(i)