# 파티가 끝나고 난 뒤
# input1 = 1m2당 사람의 수 / 파티룸의 넓이
# input2 = 각 기사에 실려있는 참가자의 수
# output = 계산한 참가자수와 각 기사에 적혀있는 참가자의 수의 차이
command = list(map(int,input().split()))
paper = list(map(int,input().split()))

people = command[0] * command[1]
for i in paper: print((i - people), end=' ')