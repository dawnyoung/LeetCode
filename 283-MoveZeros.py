"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
1) You must do this in-place without making a copy of the array.
2) Minimize the total number of operations.

             
#print([i for i in nums if i != 0]+[0]*nums.count(0))
#nums = list(filter(lambda a: a != 0, nums))
#nums = nums + [0]*n
#print(nums)

"""

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

if __name__ == '__main__':
    print(Solution().moveZeroes([0,2,3,0,1]))
