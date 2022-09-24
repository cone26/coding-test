# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
s = "()"
st = []
table = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

for bracket in s :
    if bracket not in table: st.append(bracket)
    elif not st or table[bracket] != st.pop() : print(False)

print(len(st) == 0)