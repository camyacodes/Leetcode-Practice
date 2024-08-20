from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counterHash = {}
        res = 0

        for num in nums: 
            if num in counterHash:
                res += counterHash[num]
                counterHash[num] += 1
            else:
                counterHash[num] = 1
        return res
        