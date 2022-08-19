# 암기왕
import sys
def binary_search(lst1,key,low,high):
        while low <= high:
            middle = (high+low)//2
            if key == lst1[middle]:return 1
            elif key < lst1[middle]: high = middle-1
            else: low = middle+1
        return 0
        
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst1 = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    lst2 = list(map(int,sys.stdin.readline().split()))
    lst1 = sorted(list(set(lst1)))
    for i in lst2 : print(binary_search(lst1,i,0,len(lst1)-1))
