# 24
# input 받기
current_time = list(map(int,input().split(":")))
start_time = list(map(int,input().split(":")))

# 시간 계산 함수
def calc_time(position):
    # 현재 시간보다 시작 시간의 숫자가 작다면,
    # [분, 초]의 경우 시작 [분, 초]에60을 더해주고
    # 시간의 경우 시작 시간에 24를 더해준 후 현재 시간을 빼준다.
    if start_time[position] < current_time[position]: 
        if position > 0 : 
            start_time[position] += 60
            # [분,초]의 경우 앞 자리의[시간,분] 숫자에서 1을 빼준다.
            start_time[position-1] -= 1
        else : start_time[position] += 24
        
    answer = start_time[position] - current_time[position]
    # 계산한 숫자가 10보다 작을 경우(한자리수) => 문자열로 바꿔서 출력포맷을 만들어준다. "00"
    if answer < 10 : answer = '0' + str(answer)
    return answer

second = calc_time(2)
minute = calc_time(1)
hour = calc_time(0)
print(f'{hour}:{minute}:{second}')
