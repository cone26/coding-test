# 하얀 칸
import sys
sum = 0
for i in range(1,9):
    line = sys.stdin.readline().strip()
    for j in range(1,len(line)+1):
        if i % 2 != 0 :
            if j % 2 != 0 and line[j-1] == 'F': sum += 1
        else : 
            if j % 2 == 0 and line[j-1] == 'F': sum += 1
print(sum)