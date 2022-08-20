# 단어 순서 뒤집기
n = int(input())
for j in range(n):
    sentence = input().split()
    sentence.reverse()
    print(f'Case #{j+1}:',' '.join(sentence))