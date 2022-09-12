# 819
from collections import Counter
from itertools import count
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 전처리 => 소문자, only alpabet, remove banned
words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
if word not in banned]
counts = Counter(words)
print(words)
print(counts)
print(counts.most_common()[0][0])
