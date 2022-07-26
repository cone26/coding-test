# 심부름 가는 길
# 입력받은 초를 다 더해서 분/초로 출력하기
sum = 0
for _ in range(4): sum += int(input())
print(sum // 60) ; print(sum % 60)