"""
Given scores of N athletes, find their relative ranks and the people with the
top three highest scores,who will be awarded medals: "Gold Medal", "Silver
Medal" and "Bronze Medal".

Example:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so
they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks
according to their scores.

Input: [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Note:
1) N is a positive integer and won't exceed 10,000.
2) All the scores of athletes are guaranteed to be unique.
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rank = dict((n, i+1) for i, n in \
                    enumerate(sorted(nums, reverse=True)))
        return [["Gold Medal", "Silver Medal", "Bronze Medal"][rank[x]-1] \
                if rank[x] <= 3 else str(rank[x]) for x in nums]

            

    # It works, but it is very slow
    def findRelativeRanks2(self, nums):
        scores = sorted(nums, reverse = True)
        rank = []
        for i in range(len(nums)):
            rank.append(str(scores.index(nums[i])+1))
            if scores.index(nums[i]) == 0:
                rank[i] = 'Gold Medal'
            if scores.index(nums[i]) == 1:
                rank[i] = 'Silver Medal'
            if scores.index(nums[i]) == 2:
                rank[i] = 'Bronze Medal'
            
        return rank
                        

if __name__ == '__main__':
    print(Solution().findRelativeRanks([10,3,8,9,4]))
    print(Solution().findRelativeRanks2([1,3,2,5,4]))
    
