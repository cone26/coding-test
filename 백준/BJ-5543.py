# 상근날드
# 리스트의 [0:3]까지는 햄버거고 [3:]은 음료수인데 둘을 더해서 가장 싼 세트의 가격을 출력 (합에서 -50)
menu = []
for _ in range(5): menu.append(int(input()))
sum = menu[0]
for i in menu[1:3]: 
    if i < sum : sum = i 
sum = sum + menu[3] if menu[3] < menu[4] else sum + menu[4]
print(sum - 50)