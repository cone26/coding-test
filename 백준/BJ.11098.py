# 첼시를 도와줘!
n = int(input())
for _ in range(n):
    players = [(input().split()) for _ in range(int(input()))]
    for i in players:i[0] = int(i[0])
    players.sort()
    print(players[-1][1])