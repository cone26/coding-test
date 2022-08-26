# 뒤집힌 덧셈
x,y = input().split()
sum = str(int(x[::-1])+int(y[::-1]))
print(int(sum[::-1]))

