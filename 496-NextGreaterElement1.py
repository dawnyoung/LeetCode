class Solution(object):
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2.Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    1) For number 4 in the first array, you cannot find the next greater number
       for it in the second array, so output -1.
    2) For number 1 in the first array, the next greater number for it in the
       second array is 3.
    3) For number 2 in the first array, there is no next greater number for it
       in the second array, so output -1.
"""
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = len(findNums) # nums1
        l2 = len(nums)     # nums2
        out = []
        for i in range(l1):
            n = findNums[i]
            begin = nums.index(n)
            if n >= max(nums[begin:l2]):    # if there is no greater value
                out.append(-1)              # append -1
            else:
                for j in range(begin, l2):  # if there is greater value
                    if n < nums[j]:
                        out.append(nums[j]) # append the 1st greater value
                        break               # then break the loop
        return out
