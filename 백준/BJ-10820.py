# 문자열 분석
from curses.ascii import islower


while True:
    try:
        upper, lower, digit,empty = 0,0,0,0
        line = input()
        for i in line:
            if i.isupper():upper += 1
            elif i.islower():lower += 1
            elif i.isdigit():digit += 1
            else : empty += 1
        print(lower,upper,digit,empty)
    except EOFError: break