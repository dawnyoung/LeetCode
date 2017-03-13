"""
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            num = sum(map(int, str(num)))
        return num


    # Not using loop
    
    # If the integer is 1000a+100b+a0c+d,
    # (1000a+100b+a0c+d)%9 = (a+b+c+d)%9
    
    def addDigits2(self, num):
        if num == 0:
            return 0
        elif num%9 != 0:
            return num%9
        elif num%9 == 0:
            return 9


if __name__ == '__main__':
    print(Solution().addDigits(38))
