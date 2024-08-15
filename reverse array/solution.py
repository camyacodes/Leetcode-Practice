from typing import List


class Solution: 
    def reverseArray(self, arr: List[int]) -> List[int]:
        start = 0
        end = len(arr) - 1
        temp = 0

        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

        return arr