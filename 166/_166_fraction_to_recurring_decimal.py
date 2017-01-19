"""
 166. Fraction to Recurring Decimal

    Total Accepted: 40323
    Total Submissions: 245834
    Difficulty: Medium
    Contributors: Admin

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # Directly implement division: sign => integer part => dot => decimal part
        ans = '-' if denominator*numerator < 0 else ""      # modify the sign
        numerator, denominator = abs(numerator), abs(denominator)

        ipart = abs(numerator)//abs(denominator)            # integer part
        ans += str(ipart)

        if ipart*denominator != numerator: ans += '.'       # dot

        remainder, dpart = numerator-ipart*denominator, ''  # remainder and decimal part
        rmds = {remainder: 0}

        # repeating should be check in reverse order
        # e.g. 0.0120
        #        <-- are the remainders already appeared?
        while remainder:                                    # check each remainder's appearance
            tmp = ((10*remainder)//denominator)
            dpart = dpart+str(tmp)                          # extend the decimal part
            remainder = 10*remainder - tmp*denominator
            
            start = self.checker(rmds, remainder)           # check the repeatition
            if start != -1: return ans+dpart[:start]+"("+dpart[start:]+")"
            rmds[remainder] = len(rmds)                     # if never seen => add into dict
        return ans+dpart

    def checker(self, rmds, r):      # check whether there's a repeat in decimal part
        return rmds[r] if r in rmds else -1