# 동전0
import sys
n, k = map(int,sys.stdin.readline().split())
coins=[]
count = 0
for _ in range(n): 
    coin = int(sys.stdin.readline())
    if coin <= k : coins.append(coin)
coins = sorted(coins,reverse=True)
for i in coins :
    sum = k // i
    if sum >= 1 : 
        k -= i * sum
        count += sum
print(count)