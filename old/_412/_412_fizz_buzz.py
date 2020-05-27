"""
 412. Fizz Buzz

    Total Accepted: 8451
    Total Submissions: 14603
    Difficulty: Easy
    Contributors: Admin

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number,
and for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output FizzBuzz".

Example:
n = 15,
Return:
["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""
class Solution(object):
    """ Leetcode Q412 """
    def fizzBuzz(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = [str(i) for i in xrange(1, num+1)]
        res[2::3] = ['Fizz' for _ in xrange(num//3)]
        res[4::5] = ['Buzz' for _ in xrange(num//5)]
        res[14::15] = ['FizzBuzz' for _ in xrange(num//15)]
        return res
        