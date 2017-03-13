"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):

    # This should work but it exceeds the time limit
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dis = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                dis.append(i)
        return dis


    # a better way
    def findDisappearedNumbers2(self, nums):
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        dis = []
        for i, n in enumerate(nums):
            if n > 0:
                dis.append(i+1)
        return dis
                
if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(Solution().findDisappearedNumbers2([4,3,2,7,8,2,3,1]))
