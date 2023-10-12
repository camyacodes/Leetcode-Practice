class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # Dictionary to store numbers and their indices
    
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement required to reach the target
        
        # If the complement is in the dictionary, return its index along with the current index
            if complement in num_dict:
                return [num_dict[complement], index]
        
        # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = index
    
    # If no solution is found, return an empty list or raise an exception, depending on the requirements
        return []