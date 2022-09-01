# 할로윈의 사탕
N = int(input())
for _ in range(N):
    candy,num = map(int,input().split())
    print(f'You get {candy//num} piece(s) and your dad gets {candy%num} piece(s).')
