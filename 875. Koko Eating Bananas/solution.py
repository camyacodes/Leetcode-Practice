class Solution:
    def can_eat_bananas(self, piles: List[int], h: int, k: int) -> bool:
        hours_used = 0
        for p in piles: 
            hours_used += math.ceil(float(p/k))
        return hours_used <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1000000000
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.can_eat_bananas(piles, h, mid):
                ans = mid 
                right = mid - 1
            else: left = mid + 1
        return ans