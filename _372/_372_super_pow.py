"""
 372. Super Pow

    Total Accepted: 11058
    Total Submissions: 33564
    Difficulty: Medium
    Contributors: Admin

Your task is to calculate a^b mod 1337 where a is a positive integer,
and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8

Example2:

a = 2
b = [1,0]

Result: 1024
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # Get (a^b)%1337 by implement Euler's totient function:  https://goo.gl/04exsj
        # 1337 = 7*191, phi(1337) = (7-1)*(191-1) = 6*191 = 1140
        # if a%1337 == 0: return 0
        # if a%7 == 0 (a=(7^n)*x) but a%191 != 0 (vice versa): 
        # if a%7 != 0 and a%191 != 0: (a^b)%1337 = (a^(b%1140))%1337
        return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)