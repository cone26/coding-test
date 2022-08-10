# 좋은 단어

n = int(input())
count = 0
for _ in range(n):
    st = []
    alphabets = input()
    for i in alphabets:
        if st[-1] == i : st.pop()
        elif st[-1] == i : st.pop()
        else : st.append(i)
    if len(st) == 0 : count += 1
print(count)
