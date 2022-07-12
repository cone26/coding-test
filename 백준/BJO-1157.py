# 단어 공부
import sys 
word = sys.stdin.readline().strip().lower()
wordSet = list(set(word))
cnt = []
for i in wordSet:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2 : print('?')
else : print(wordSet[(cnt.index(max(cnt)))].upper())