class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Clarify: is the arr sorted? 
        #  edge cases:
            # k = 0
            #  arr is empty

        # given and array and int find the k most frequent elements in the arr. return in any order
        # nums = [1,2,2,3,3,3], k = 2 Answer: [2,3] bc 2 & 3 are the 2 most frequent elements in the arr
        # nums = [7,7], k = 1 Ans: [7] bc 7 is the 1st or MOST frequent arr
        # nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6], k = 3 Ans: [3, 4, 5] bc they are the top 3 elems

        # TEST CASE nums = [1,2,2,3,3,3], k = 2 Answer: [2,3]

        # create hashmap
        count = {}
        # create empty arr that will contain subarrs for each count possible max is length of arr
        freq = [[] for i in range(len(nums) + 1)]

        # loop through arr and find count of each num add it to hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0) # count = {1: 1, 2: 2, 3: 3}
        # loop through hashmap key value pair and add the num to the frequency arr at the subarr at the count index
        for n, c in count.items():
            freq[c].append(n) # freq = index/count  0  1   2   3  4  5  6  7
            #                          nums        [] [1] [2] [3] [] [] [] []
        # res is arr of top elems initialize size limit is k
        res = []
        # loop through freq arr of subarrs starting at the top to get most elems
        for i in range(len(freq) - 1, 0, -1):
            # for each number in subarr at that count
            for n in freq[i]:
                # add to res
                res .append(n)
                # if res is big enough return it
                if len(res) == k:
                    return res #[3,2]
        
        
