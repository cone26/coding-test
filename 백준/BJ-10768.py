# 특별한 날
N = int(input())
M = int(input())

if N < 2 : print('Before')
elif N > 2 :print('After')
elif N == 2 : 
    if M < 18 : print('Before')
    elif M > 18 : print('After')
    else : print('Special')