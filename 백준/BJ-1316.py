# 그룹 단어 체커
n = int(input())
count = 0; answer = True
for _ in range(n): 
    word_list = [] 
    word = input()
    for i in range(len(word)):
        if word[i] not in word_list: word_list.append(word[i])
        else:
            if word[i-1] != word[i] : 
                answer = False
                break
    if answer == True: count += 1
    answer = True
print(count)