"""
Given a List of words, return the words that can be typed using letters of alphabet on
only one row's of American keyboard like the image below.

First row: qwertyuiop
Second row: asdfghjkl
Thrid row: zxcvbnm

Note:
1) You may use one character in the keyboard more than once.
2) You may assume the input string will only contain letters of alphabet.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

class Solution(object):


    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm') # difine the reference letters
        targetwords = []
        for word in words:
            wordset = set(word.lower()) # case sensitive
            if wordset.issubset(row1) or wordset.issubset(row2) or wordset.issubset(row3):
                targetwords.append(word) # save the qualified word into the output list
        return targetwords

if __name__ == '__main__':
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
