# 스택수열
import sys
n = int(sys.stdin.readline())
count = 1
num_list=[]
st=[]
answer = []
temp = True
for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        st.append(count)
        answer.append('+')
        count += 1
    if st[-1] == num:
        st.pop()
        answer.append('-')
    else : 
        temp = False

if temp != True: print('NO')
else :
    for j in answer:print(j)
