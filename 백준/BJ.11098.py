# 첼시를 도와줘!
# 총 반복 수
n = int(input())
for _ in range(n):
    # 선수 명단 입력
    players = [(input().split()) for _ in range(int(input()))]
    # 선수 명단에서 각 첫번째 자리는 금액임 => int로 형변환
    for i in players:i[0] = int(i[0])
    # 오름차순으로 정렬
    players.sort()
    # 리스트 마지막 요소의 마지막 값 (이름) 출력
    print(players[-1][1])