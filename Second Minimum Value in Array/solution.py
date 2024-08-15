from typing import List
import math

class Solution: 
    def secondMin(self, nums: List[int]) -> int:
        max = -math.inf
        second_max = -math.inf

        for num in nums:
            if num > max:
                second_max = max
                max = num
            elif num > second_max and num != max:
                second_max = num
        
        return second_max