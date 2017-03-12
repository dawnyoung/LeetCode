class Solution(object):
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    
Note:
1) The input array will only contain 0 and 1.
2) The length of input array is a positive integer and will not exceed 10,000
"""
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = []
        size = 0 # the size of the longest one sequence
        for i in nums:
            if i == 1:
                ones.append(i)
                if size < len(ones):
                    size = len(ones) # save the length of the longer sequence
            if i == 0:
                ones = [] # reset when 0 appears
        return size
