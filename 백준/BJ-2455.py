# 지능형 기사
count = 0
peak = 0
for _ in range(4):
    people_out, people_in = map(int,input().split())
    count -= people_out
    count += people_in
    if count >= peak : peak = count
print(peak)