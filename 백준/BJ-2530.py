# 인공지능 시계
# 인풋 : 시 분 초
# 인풋2 : 필요한 시간(초단위)
# 인풋2를 인풋1[2]에 더해서 => 그 값을 60으로 나눈 몫을 저장하고 나머지를 인풋1[2]에 넣어주기 
# 저장한 몫 값을 60으로 나눠서 몫이 1이상이라면 그 값을 인풋1[0]에 더해주고 나머지는 인풋1[1]에 넣기

current_time=list(map(int,input().split()))
cooking_time = int(input())

current_time[2] = cooking_time + current_time[2]
if current_time[2] // 60 >= 1 : 
    current_time[1] += current_time[2] // 60
    current_time[2] = current_time[2] % 60
if current_time[1] // 60 >= 1 :
    current_time[0] += current_time[1] // 60
    current_time[1] = current_time[1] % 60
if current_time[0] >= 24 : current_time[0] = current_time[0] % 24
print(f'{current_time[0]} {current_time[1]} {current_time[2]}')