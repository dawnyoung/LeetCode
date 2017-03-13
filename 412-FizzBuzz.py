"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”.For numbers which are multiples of
both three and five output “FizzBuzz”.

"""

class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        outlist = []
        for i in range(1, n+1): # remember to use n+1 in the range
            if i%3 == 0 and i%5 == 0:
                outlist.append('FizzBuzz')
            elif i%3 == 0 and i%5 != 0:
                outlist.append('Fizz')
            elif i%3 != 0 and i%5 == 0:
                outlist.append('Buzz')
            else:
                outlist.append(str(i))
        return outlist


if __name__ == '__main__':
    print(Solution().fizzBuzz(30))
