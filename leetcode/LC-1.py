# two sum
# 브루트포스 => 5389 ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if (nums[i] + nums[j]) == target: return [i,j]

# in을 이용 => 937 ms
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums and i != nums.index(target-nums[i]): return [i,nums.index(target-nums[i]) ]

# 책 답변 => 730 ms
class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            if (target - num) in nums[i+1:]: return [i,nums[i+1:].index(target-num) +(i+1) ]

# dict를 사용한 바로 조회 => 102 ms
class Solution(object):
    def twoSum(self, nums, target):
        nums_map={}
        for i, n in enumerate(nums): nums_map[n] = i
        for i, n in enumerate(nums):
            if target-n in nums_map and i != nums_map[target-n]: return [i,nums_map[target-n]]
# dict 조회 O(1)

# 위 코드 개선 => 77ms
class Solution(object):
    def twoSum(self, nums, target):
        nums_map={}
        for i, n in enumerate(nums):
            if target-n in nums_map: return [nums_map[target-n],i]
            nums_map[n] = i

            