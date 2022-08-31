# 내 학점을 구해줘
T = int(input())
for _ in range(T):
    N = int(input())
    c_sum,g_sum = 0,0.0
    for _ in range(N):
        C,G = input().split()
        c_sum += int(C)
        g_sum += float(G) * int(C)
    print(c_sum,round(g_sum / c_sum,1))