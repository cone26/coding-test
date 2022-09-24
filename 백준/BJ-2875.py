# 대회 or 인턴
w,m,i = list(map(int, input().split()))
if w > m : w -= i
else : m -= i
if w // 2 > m : print(0)
print(w // 2)

# if (m - i) > w // 2 : print(team)
# elif (i / 2) > 1 : print(team - (i//2+1))
# else : print(team - 1)