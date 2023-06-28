str = input()
for i in str:
    print(i.upper() if i.islower() else i.lower(), end="")



# 다른 사람 답
print(str.swapcase())