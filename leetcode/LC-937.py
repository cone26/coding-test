# Reorder Data in Log Files
from curses.ascii import isdigit


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

digits,letters=[],[]
# logs를 돌면서
for log in logs:
# 어떤 로그인지 확인(숫자, 문자)
    if log.split()[1].isdigit(): digits.append(log)
# 숫자로그라면 숫자 배열에 넣고
# 문자 로그라면 문자 배열에 넣어줌
    else : letters.append(log)
# 문자 로그는 문자로 sort하고 겹치면 identifier로 sort
letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
print(letters+digits)