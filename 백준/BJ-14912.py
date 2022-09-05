# 숫자 빈도수
from collections import Counter
N,M = input().split()
count = 0
for i in range(1,int(N)+1) :
    c = Counter(str(i)).most_common()
    for j in c : 
        if j[0] == M : count += j[1]
print(count)