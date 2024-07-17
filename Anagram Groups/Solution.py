from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # create defaultdict where you map character count to list of strings
            res = defaultdict(list)
            # loop through array of strings
            for s in strs:
            # create list of 26 zeros to represent count of characters of the alphabet
                count = [0] * 26
            # for each character in string
                for char in s: 
            # add 1 to position in array (Calculated by ascii numerical form minus a ascii number)
                    count[ord(char) - ord('a')] += 1
            # then add that string to the key which is the count TUPLE
                res[tuple(count)].append(s)
            # return just the values of the hashmap
            return res.values()