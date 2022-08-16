import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for _ in range(n):nums.append(int(sys.stdin.readline().rstrip()))

print(round(sum(nums)/n))

sorted_nums = sorted(nums)
print(sorted_nums[n//2])

cnt = Counter(sorted_nums)
tmp = cnt.most_common()

if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(sorted_nums[-1]-sorted_nums[0])