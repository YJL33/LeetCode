"""
 7. Reverse Integer

    Total Accepted: 203936
    Total Submissions: 860888
    Difficulty: Easy
    Contributors: Admin

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
class Solution(object):
    """Solution of Leetcode #7"""
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        res, x = 0, abs(x)
        while x != 0:
            res, x = res*10+(x%10), x/10
            # print res, x

        return sign*res if abs(res) < 0x7fffffff else 0

# def main():
#     """ code here """
#     numlist = [123, -123, 150, 999999, 1]
#     print map(Solution().reverse, numlist)

if __name__ == "__main__":
    main()
