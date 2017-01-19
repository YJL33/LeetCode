"""
415. Add Strings

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

IMPORTANT:
Solutions which uses a BigInteger library or converting the input strings to another type
(such as integer) will result in disqualification of all submissions to this problem.
After the contest ends, users can view accepted submissions code and report cheating solutions.

Given two non-negative numbers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs
    to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j, carry, res = 0, 0, 0, []

        while i < len(num1) or j < len(num2) or carry:
            if i < len(num1):
                carry += ord(num1[::-1][i])-48      # get the value
                i = i+1                             # and move on
            if j < len(num2):
                carry += ord(num2[::-1][j])-48
                j = j+1
            res += carry%10,
            carry //= 10                            # carry to next digit

        ans = ""
        for c in res[::-1]:
            ans += chr(c+48)

        return ans