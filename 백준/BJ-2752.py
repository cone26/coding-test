# 세수정렬
# 숫자들을 리스트로 받은 다음에 => sorted?
nums = list(map(int,input().split()))
sorted_list = sorted(nums)
print(' '.join(str(e) for e in sorted_list))