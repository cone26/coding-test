#  소수 구하기
import sys
m, n = map(int,sys.stdin.readline().split())

def isPrime(num) :
    if num == 1 : return False
    for j in range(2,int(num ** 0.5) + 1): 
        if num % j == 0: return False
    return True

for i in range(m, n+1): 
    if isPrime(i) : print(i)

#  그냥 평소에 소수 구하던 것 처럼 하나하나 반복문을 돌면서
#  구하면 시간 초과가 뜬다 ! 마지막 수까지 다 반복문 돌 필요 없이
#  마지막 수의 제곱근까지만 돌면 됨