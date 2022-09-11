nums = [-1,0,1,2,-1,-4]

# # 브루트포스
# answer = []
# # 중복 값을 거르기 위한 작업
# nums.sort()

# # 브루트포스
# for i in range(len(nums)-2):
#     # 중복 필터
#     if i > 0 and nums[i] == nums[i-1] : continue
#     for j in range(i+1, len(nums)-1):
#         # 중복 필터
#         if j > i+1 and nums[j] == nums[j-1] : continue
#         for k in range(j+1, len(nums)):
#             # 중복 필터
#             if k > j+1 and nums[k] == nums[k-1] : continue
#             if nums[i] + nums[j] + nums[k] == 0 : answer.append([nums[i],nums[j],nums[k]])
# print(*answer)
# 투 포인터
answer = []
nums.sort()

for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1] : continue
    # pointer setting
    left, right = i + 1, len(nums)-1
    # 값 좁히며 더하기
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0 : left += 1
        elif sum > 0 : right -= 1
        else : 
            # sum이 0이라면
            answer.append([nums[i], nums[left],nums[right]])
            while left<right and nums[left] == nums[left+1]: left += 1
            while left<right and nums[right] == nums[right-1]: right -= 1
            left += 1
            right -= 1

print(answer)