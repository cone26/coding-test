# 과자
# input 돈 가격/ 갯수/ 현재 가진 돈 
# output 추가로 필요한 돈
info = list(map(int, input().split()))
amount = info[0] * info[1]
if (amount - info[2]) < 0 : print(0)
else : print(amount - info[2])