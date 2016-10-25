"""
 224. Basic Calculator

    Total Accepted: 37625
    Total Submissions: 152954
    Difficulty: Hard
    Contributors: Admin

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces.

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function.
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # scan from beginning.
        # if meet a new sign: wrap up the result, and reset num=0 and sign (as the new sign)
        # if meet a left "(": put the result and sign into temperatory stack, then reset them.
        # if meet a right "(": wrap up the result in (), and combine with the last one in stack.
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)       # get the number
            elif c in ["-", "+"]:
                res += sign*num             # calculate the result
                num = 0                     # reset the number and sign
                sign = [-1, 1][c=="+"]
            elif c == "(":
                stack.append(res)           # put previous result into stack
                stack.append(sign)
                sign, res = 1, 0            # and reset the result and sign
            elif c == ")":
                res += sign*num             # close the result inside the ()
                res *= stack.pop()          # and combine with previous result
                res += stack.pop()
                num = 0                     # reset the number
        return res + num*sign