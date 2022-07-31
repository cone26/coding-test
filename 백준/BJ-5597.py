# 과제 안 내신 분
from turtle import home


student=[]
homework=[]
for i in range(1,31): student.append(i)
for _ in range(28): homework.append(int(input()))
for j in student:
    if j not in homework : print(j)