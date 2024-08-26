class Solution: 
    def targetPosition(self, nums: int, target: int) -> int:
        left, right = 0, len(nums) # target could have to be inserted all the way at the end so we do len(nums) instead of len - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else: 
                left = mid + 1
        
        return left