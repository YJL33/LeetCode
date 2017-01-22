"""
439. Ternary Expression Parser

    User Tried: 1
    Total Submissions: 1
    Difficulty: Medium

Given a string representing arbitrarily nested ternary expressions,
calculate the result of the expression.
You can always assume that the given expression is valid and only consists of digits 0-9, ?, :,
T and F (T and F represent True and False respectively).

Note:
The length of the given string is <= 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.

"""
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        while len(expression) != 1:
            i = expression.rindex("?")    # begin with the last '?'.
            tmp = expression[i+1] if expression[i-1] == 'T' else expression[i+3]
            expression = expression[:i-1] + tmp + expression[i+4:]
        return expression
