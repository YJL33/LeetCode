"""
8
"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # convert a string to 32bit signed integer
        # range [-2^31, 2^31-1]

        # check if there's leading whitespace
        # check if there's +/-
        # check if it's non-digit
        # check if the number is within the range

        isPositive = True
        noMoreSpaceOrSign = False
        num = 0
        
        for i in range(len(s)):
            if not noMoreSpaceOrSign and s[i] == ' ':
                continue
            elif not noMoreSpaceOrSign and s[i] in "+-":
                noMoreSpaceOrSign = True
                isPositive = False if s[i] == "-" else True
            elif s[i] in '0123456789':
                noMoreSpaceOrSign = True
                num = num*10+int(s[i])
            else:
                break
        
        if isPositive:
            return min(2147483647, num)
        else:
            num *= -1
            return max(-2147483648, num)