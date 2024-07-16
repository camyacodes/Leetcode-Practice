class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create empty dict val: index
        seenMap = {}
        # loop through nums
        for index, num in enumerate(nums):
        # calculate complement to the num
            diff = target - num
        # look for it in the hashmap
            if diff in seenMap:
        # if its there, return compliment index in hashmap and index of num
                return [seenMap[diff], index]
        # if not there add num: index to hashmap
            seenMap[num] = index
        # return if no pair found
        return