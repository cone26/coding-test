# 영수증
import sys
amount = int(sys.stdin.readline().strip())
for _ in range(9): amount -= int(sys.stdin.readline().strip())
print(amount)