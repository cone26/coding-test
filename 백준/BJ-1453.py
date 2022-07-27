# 피시방 알바
n = int(input())
customers = input().split()
count = 0
seat =[]
for i in customers: 
    if i in seat : count += 1
    seat.append(i)
print(count)