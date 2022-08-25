# 이진수
num = int(input())
for _ in range(num):
    n = int(input())
    b = format(n,'b')[::-1]
    for i in range(len(b)): 
        if b[i] == '1': print(i,end=' ')