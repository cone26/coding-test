input = input()
answer = ''
for i in input:
    char = ord(i) - 3
    if char < 65: answer += chr(char + 26)
    else: answer += chr(char)
print(answer)