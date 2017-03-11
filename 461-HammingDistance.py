class Solution(object):
"""
Hamming Distance

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

0 ≤ x, y < 2**31

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:] # convert integer to bit and leave out '0b'
        l_x = len(str(x))
        l_y = len(str(y))
        n = 0
        if l_x >= l_y:
            x2 = x[(l_x-l_y):]
            for i in range(l_y):
                if x2[i] != y[i]:
                    n += 1
            n = x[0:l_x-l_y].count('1')+n
        if l_y > l_x:
            y2 = y[(l_y-l_x):]
            for i in range(l_x):
                if x[i] != y2[i]:
                    n += 1
            n = y[0:l_y-l_x].count('1')+n
        return n

    # the best way
    def hammingDistance2(self, x, y):
        return bin(x^y).count('1') 
