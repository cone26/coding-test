# 캠핑]
count = 0
while True:
    count += 1
    L,P,V = map(int,input().split())
    if L+P+V == 0: break
    answer = 0
    answer += (V // P) * L
    if V % P < L : answer += V % P
    print(f'Case {count}: {answer}')