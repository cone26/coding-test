# 집주소
import sys

while 1:
    nums = sys.stdin.readline().strip()
    if nums == '0' : break
    sum = len(nums) + 1
    for i in nums:
        if i == '1' : sum += 2
        elif i == '0' : sum += 4
        else : sum += 3
    print(sum)