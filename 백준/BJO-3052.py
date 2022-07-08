# 나머지
import sys
nums = []
for _ in range(10):
    n = int(sys.stdin.readline()) % 42
    nums.append(n)

nums_set = set(nums); 
print(len(nums_set))