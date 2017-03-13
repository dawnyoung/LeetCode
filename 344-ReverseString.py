"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        news = ''
        for i in range(len(s)):
            news += s[len(s)-i-1]
        return news


    # A better way
    def reverseString2(self, s):
        return s[::-1]


if __name__ == '__main__':
    print(Solution().reverseString('hello'))
    print(Solution().reverseString2('hello'))
