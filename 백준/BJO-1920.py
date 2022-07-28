# 수 찾기
# 이분탐색
import sys
n1 = int(sys.stdin.readline().strip())
first_list = set(map(int,sys.stdin.readline().strip().split()))
n2 = int(sys.stdin.readline().strip())
second_list = list(map(int,sys.stdin.readline().strip().split()))
# for j in second_list:
#     if j in first_list : print(1)
#     else : print(0)


# def binary (i, lis1, low, high):
#     if low > high : return 0
#     mid = (low+high) //2
#     if i == lis1[mid] : return 1
#     elif i < lis1[mid] :return binary(i,lis1, low , mid-1)
#     else : return binary(i,lis1, mid + 1,high)

# for i in second_list:
#     low,high = 0, (n1 - 1)
#     print(binary(i,first_list,low,high))
for i in second_list:
    if i in first_list: print(1)
    else : print(0)