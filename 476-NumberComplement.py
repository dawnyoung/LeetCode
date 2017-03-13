"""
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary
representation.

Note:

1) The given integer is guaranteed to fit within the range of a 32-bit signed
integer.

2) You could assume no leading zero bit in the integer’s binary representation.
"""

class Solution(object):


    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num) # convert integer to bit
        new  = 0       # set initial value
        for i in range(2, len(str(num))):
            if num[i] == '0':
                new += 2**(len(str(num))-i-1) # calculate the complement number
        return new


if __name__ == '__main__':
    print(Solution().findComplement(4))
