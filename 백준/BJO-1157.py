# 단어 공부
import sys 
# word = sys.stdin.readline().strip().lower()
# wordSet = list(set(word))
# cnt = []
# for i in wordSet:
#     count = word.count(i)
#     cnt.append(count)

# if cnt.count(max(cnt)) >= 2 : print('?')
# else : print(wordSet[(cnt.index(max(cnt)))].upper())
from collections import Counter
word = sys.stdin.readline().strip().lower()
common = Counter(word).most_common()
if len(common) >= 2 and common[0][1] == common[1][1]: print('?')
else : print(common[0][0].upper())