# 평균 점수
# 점수가 40점 미만인 학생의 점수 => 40 => 학생들의 평균 구하기
sum = 0
for _ in range(5):
    score = int(input())
    if score < 40 : score = 40
    sum += score
print(sum // 5)
