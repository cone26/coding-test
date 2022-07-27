# 직사각형에서 탈출
x,y,w,h = list(map(int,input().split()))
distance = []
distance.append(w - x); distance.append(h-y)
distance.append(-(0-x)); distance.append(-(0-y))
print(min(distance))