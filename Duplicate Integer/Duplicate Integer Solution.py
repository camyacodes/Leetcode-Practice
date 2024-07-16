class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  create empty hashmap val: index
        seenSet = set()
        # loop through array
        for n in nums:
        # check if number is in hashmap
            if n in seenSet: 
        #if so return true
                return True
        #if not add to hashmap
            seenSet.add(n)
        # get the end and no duplicates return false
        return False
    