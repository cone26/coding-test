# # 세로읽기
# phrase = []
# for _ in range(5):phrase.append(input().strip())
# longest = phrase[0]
# # for i in phrase : 
# #     if len(phrase) > len(longest) : longest = i
# # for i in range(len(longest)):
# #     for j in phrase:
# #         if len(j)-1 < i: continue
# #         print(j[i],end='')
# for i in phrase:
#     for j in i:
#         if j == " ": continue
#         print(j,end='')