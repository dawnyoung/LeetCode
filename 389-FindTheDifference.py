class Solution(object):
"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more
letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t)) # letters can be in different order, so sort first
        diff = ''
        for i in range(len(s)):
            if s[i] != t[i]:
                diff = t[i]
                break # stop once find the mismatch (added one)
        if diff == '':
            diff = t[-1] # return the last letter if the added letter is at the end
        return diff
