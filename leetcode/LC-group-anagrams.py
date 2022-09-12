# 49

from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
# dic 생성
anagrams = defaultdict(list)
# strs를 돌면서 
for str in strs :
# 단어마다 정렬한 후 
    anagrams[''.join(sorted(str))].append(str)
    # sorted는 list를 반환하기 때문에 다시 문자열로 만들어주기
# 그 단어를 키로 가지는 dict 리스트 안에 그 단어를 넣어줌
print(list(anagrams.values()))
# anagrams가 dict값이기 때문에 다시 ㅣist로 비꿔주기