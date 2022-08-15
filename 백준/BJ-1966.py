# 프린터 큐
num = int(input())
for _ in range(num):
    n,m = list(map(int, input().split()))
    printer = list(map(int,input().split()))
    pointer = m
    count = 0
    if len(printer) == 1: print(1)
    else :
        while True:
            if printer[0] != max(printer) : 
                printer.append(printer.pop(0))
                if pointer == 0 : pointer = len(printer)
            else :
                printer.pop(0)
                count += 1
                if pointer == 0 : break
            pointer -= 1
        print(count)

    