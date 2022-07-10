# 제로
import sys
n = int(sys.stdin.readline().strip())
st = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    st.pop() if num == 0 else st.append(num)
print(sum(st))