class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        
        for i in range(1, len(f) - 1):
            if f[i] == 0 and f[i - 1] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

# 3 000's means you can plant a flower
# BUT account for empty plots outside original array