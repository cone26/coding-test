# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# import sys
# worst = []
# n,m = map(int,sys.stdin.readline().split())
# for _ in range(m): worst.append(list(map(int,sys.stdin.readline().split())))
# icecream = [ x for x in range(1,n+1)]
# count = 0
# minus = 0
# for i in range(0,len(icecream)-2):
#     for j in range(i+1, len(icecream)-1):
#         for k in range(j+1,len(icecream)):
#             count += 1
#             mix = [icecream[i],icecream[j],icecream[k]]
#             for q in worst:
#                 if q[0] in mix and q[1] in mix: 
#                     continue
#                     break
# print(count)