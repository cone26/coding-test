import sys
n, m = list(map(int,sys.stdin.readline().split()))
lan = []
for _ in range(n): lan.append(int(sys.stdin.readline()))
low, high = 1, max(lan)
while low <= high:
    sum = 0
    mid = (low + high) //2 
    for i in lan : sum += i // mid
    if sum >= m : low = mid + 1
    else : high = mid -1
print(high)