class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashMapS = {}
        res = 0

        for i in range(0, len(s)):
            hashMapS[s[i]] = i

        for i in range(0, len(t)):
            res += abs(hashMapS[t[i]] - i)
        return res
        