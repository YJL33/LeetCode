"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument,
please click the reload button to reset your code definition.
"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, sign, cur = 0, 1, 0

        while cur < len(s):
            if s[cur] == ' ':
                cur += 1
            elif s[cur] == '-':
                sign, cur = -1, cur+1
                break
            elif s[cur] == '+':
                cur += 1
                break
            elif ord(s[cur]) > 57 or ord(s[cur]) < 48:
                cur += len(s)
            else:
                break

        while cur < len(s) and ord(s[cur]) <= 57 and ord(s[cur]) >= 48:
            res, cur = res*10+(ord(s[cur])-48), cur+1
            
        res *= sign

        if res>0:
            return min(res, 2147483647)
        else:
            return max(res, -2147483648)