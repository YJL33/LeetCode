"""
43. Multiply Strings
Medium

1699

773

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted
289,166
Submissions
862,795
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # implement the process of multiply on paper (by hand)
        # e.g.  125   <- num2
        #      x 12   <- num1
        #  --------
        #       250
        #      125
        #  --------
        #      1500

        # time: O(MN), space: O(N)

        rev1, rev2 = num1[::-1], num2[::-1]

        res = []
        multiply, carry = 0, 0
        for i in xrange(len(num1)):
            res += 0,
            carry = 0
            for j in xrange(len(num2)):
                a, b = int(rev1[i]), int(rev2[j])
                multiply = a*b + carry
                left, carry = multiply%10, multiply//10
                res[i] += left * (10**(i+j))
            if carry:
                res[i] += carry * (10**(i+j+1))

        return str(sum(res))

print Solution().multiply("123", "456")
print Solution().multiply("12", "125")
print Solution().multiply("2", "4")
