# 접미사 배열
word = input().rstrip()
word_list = []
for i in range(len(word)): word_list.append(word[i:])
word_list.sort()
for j in word_list:print(j) 