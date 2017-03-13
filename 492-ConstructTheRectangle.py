"""
For a web developer, it is very
important to know how to design a web page's size. So, given a specific
rectangular web page’s area, your job by now is to design a rectangular
web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given
target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.

You need to output the length L and the width W of the web page you designed
in sequence.

Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.
"""

class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        w = math.sqrt(area) # if the squre root is integer, then it is the answer
        for i in reversed(range(int(w)+1)):
            if area%i == 0:
                return [int(area/i), i]
                break


    # This should work, but takes much longer than the above one
    def constructRectangle2(self, area):
        res = [100000000,1]
        for l in range(1, area+1):
            if area%1 == 0 and l>area/l and l-area/l < res[0]-res[1]:
                res = [l, int(area/l)]
        return res

if __name__ == '__main__':
    print(Solution().constructRectangle(20))
    print(Solution().constructRectangle2(20))



