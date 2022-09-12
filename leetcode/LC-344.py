# Reverse String
# pythonic
s = ["h","e","l","l","o"]
s.reverse()
print(s)

# 투포인터
left, right = 0, len(s)-1
while left < right :
    s[left],s[right] = s[right],s[left]
    left += 1
    right -= 1
print(s)