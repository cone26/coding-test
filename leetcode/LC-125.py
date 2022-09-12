# Valid Palindrome
from curses.ascii import isalnum
import re
s = "A man, a plan, a canal: Panama"
# 슬라이싱
# 문자열 전처리 lower, only alphanumeric 
s = s.lower()
s = re.sub('[^a-z0-9]','',s)
print(s == s[::-1])

# for문 양끝에서부터 비교
answer =[]
for i in s : 
    if i.isalnum() : answer.append(i.lower())
left,right = 0, len(answer)-1
while len(answer) < 1 : 
    if answer.pop(0) != answer.pop(): print(False) 
print(True)
from collections import deque  

# Deque 양 끝에서부터 비교(최적화)
answer = deque()
for i in s :
    if i.isalnum() : answer.append(i.lower())
while len(answer) < 1:
    if answer.popleft() != answer.pop(): print(False)
print(True)