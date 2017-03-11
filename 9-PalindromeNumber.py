class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False # negative integers are not palindrome
        if x == 0:
            return True  # 0 is a palindrome number
        if len(str(x)) == 1:
            return True  # single digit is palindrome
        digits = len(str(x)) # number of digits
        for i in range(0, digits//2):
            d1 = x//(10**(digits-i-1))-x//(10**(digits-i))*10
            d2 = (x-x//10**(i+1)*10**(i+1) - x%10**i)/10**i
            if d1 != d2:
                return False # return false if there is any mismatch
        return True          # otherwise, return true
