class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
   
        max_candies = max(candies)
        target = max_candies - extraCandies

        for i in range(0, len(candies)): 
            if candies[i] < target:
                candies[i] = False
            else: candies[i] = True

        return candies