#  음계
import sys

nums = sys.stdin.readline().split()
numSor = sorted(nums)
numRe = sorted(nums, reverse=True)
if nums == numSor :print('ascending')
elif nums == numRe:print('descending')
else : print('mixed')