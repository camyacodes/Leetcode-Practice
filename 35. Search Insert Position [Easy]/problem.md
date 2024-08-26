35. Search Insert Position [Easy]
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Example:

Input: [1,3,5,6], 5
Output: 2
Input: [1,3,5,6], 2
Output: 1
Very classic application of binary search. We are looking for the minimal k value satisfying nums[k] >= target, and we can just copy-paste our template. Notice that our solution is correct regardless of whether the input array nums has duplicates. Also notice that the input target might be larger than all elements in nums and therefore needs to placed at the end of the array. That's why we should initialize right = len(nums) instead of right = len(nums) - 1.
