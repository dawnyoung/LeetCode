"""
Given an array of integers,every element appears twice except for one. Find
that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
"""
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in range(len(nums)):
            num = num ^ nums[i]
        return num

"""
Explanation

[1,2,3,2,1]

1^2^3^2^1 = (1^1)^(2^2)^3 = 0^0^3 = 3
"""

if __name__ == "__main__":
    print(Solution().singleNumber([1, 2, 3, 4, 3, 2, 1]))
