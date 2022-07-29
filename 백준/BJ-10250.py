# acm호텔

num = int(input())
count = 0
for _ in range(num):
    h,w,n=list(map(int,input().split()))
    floor = n % h
    room= (n // h) + 1
    if n % h == 0 : 
        floor = h 
        room = n // h
    print(f'{floor * 100 + room}')