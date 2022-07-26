# 삼각형 외우기
info = []
for _ in range(3): info.append(int(input()))
if info[0] == 60 and info[1] == 60 and info[2] == 60: print('Equilateral')
elif sum(info) == 180 and (info[0] == info[1] or info[1] == info[2] or info[0] == info[2]) : print('Isosceles')
elif sum(info) == 180 and (info[0] != info[1] and info[1] != info[2] and info[0] != info[2]) : print('Scalene')
else : print('Error')