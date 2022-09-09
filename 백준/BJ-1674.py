while True:
    try:
        chicken = 0
        n,k = map(int,input().split())
        if n >= k :
            chicken += n
            chicken += n // k
            if n // k >= k : chicken += (n // k) // k
        print(chicken)
    except: break