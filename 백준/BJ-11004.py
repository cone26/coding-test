# k번쨰 수
n,k = map(int,input().split())
nums = map(int,input().split())
sorted_nums = sorted(nums)
print(sorted_nums[k-1])