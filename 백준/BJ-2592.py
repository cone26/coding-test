# 대표값
from collections import Counter
lst = [int(input()) for _ in range(10)]
print(sum(lst)//10)
print(Counter(lst).most_common()[0][0])