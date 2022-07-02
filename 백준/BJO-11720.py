#  숫자의 합
import sys
n = int(sys.stdin.readline())
sum = 0
nums = map(int,list(sys.stdin.readline().strip()))
for num in nums : sum = sum + num
print(sum)