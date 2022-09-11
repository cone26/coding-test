height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 투 포인터
def trap(height):
        if not height : return 0 
#       settings
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left],height[right]
#         반복문 
        while left < right : 
#       max값 설정
            left_max = max(left_max, height[left])
            right_max = max(right_max,height[right])
#       더 큰 쪽으로 포인터 이동
            if left_max <= right_max : 
                volume += left_max - height[left]
                left += 1
            else : 
                volume += right_max - height[right]
                right -= 1
        return volume
answer = trap(height)
print(answer)