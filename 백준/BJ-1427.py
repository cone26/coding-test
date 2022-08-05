# 소트인사이드
num = list(map(int,input()))
sorted_num = sorted(num,reverse=True)
string_num = [str(n) for n in sorted_num]
print(''.join(string_num))
