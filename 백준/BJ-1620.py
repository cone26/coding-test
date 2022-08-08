# 나는야 포켓몬 마스터 이다솜
import sys
n,m = map(int,sys.stdin.readline().split())
pocketmon = {}
for i in range(1, n + 1): 
    mon = sys.stdin.readline().strip()
    pocketmon[i] = mon
    pocketmon[mon] = i
for j in range(m):
    question = sys.stdin.readline().strip()
    if question.isnumeric() : 
        print(pocketmon[int(question)])
    else : print(pocketmon[question])