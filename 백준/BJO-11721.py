# 열개씩 끊어 출력하기
import sys
inputString = sys.stdin.readline().strip()

for i in range(0,len(inputString),10) :
    print(inputString[i:i+10])