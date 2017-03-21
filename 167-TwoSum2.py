"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2. Please note that
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not
use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):

    # This works, but slowly
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                    break


    # This works when each element in the list is unique
    # It fails when numbers = [0,0,3,4], target = 0
    def twoSum2(self, numbers, target):
        for n in numbers:
            if (target-n) in numbers \
               and numbers.index(n) != numbers.index(target-n): # make sure each element is used only once
                return [numbers.index(n)+1, numbers.index(target-n)+1]

    def twoSum3(self, numbers, target):
        dict = {}
        for i in range(len(numbers)):
            x = numbers[i]
            if target-x in dict:
                return ([dict[target-x]+1, i+1])
            dict[x] = i
        


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 18))
    print(Solution().twoSum2([2, 7, 11, 15], 18))
    print(Solution().twoSum3([0,0,3,4], 0))
