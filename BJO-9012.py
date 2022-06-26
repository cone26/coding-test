# 괄호
# 몇 번 반복할건지 입력
import sys
T = int(sys.stdin.readline())

# 괄호를 비교한는 괄호
def checkBrackets(command):
    stack = []
    for i in command:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0: return 'NO'
            else : stack.pop(-1)
    if len(stack) != 0 : return 'NO'
    else : return 'YES'
        
# 입력받은 n만큼 함수를 반복 
for _ in range(T):
    command = sys.stdin.readline()
    result = checkBrackets(command)
    print(result)