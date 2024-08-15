class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0 and nums[j] == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            if nums[j] != 0:
                j += 1