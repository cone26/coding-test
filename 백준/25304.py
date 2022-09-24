total_amount = int(input())

sum = 0
for i in range(int(input())):
    price, count = map(int,input().split())
    sum += (price * count)
if total_amount == sum : print('Yes')
else : print("No")