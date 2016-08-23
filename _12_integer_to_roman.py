"""
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # check each digit, and assign it.
        # http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
        a, b, c, d = num/1000, (num%1000)/100, (num%100)/10, (num%10)
        #print '\n',a, b, c, d
        nums = [a,b,c,d]
        roman = ['I','V','X','L','C','D','M','quinque_milia','decem_milia']
        res = ''
        d = 0
        for n in nums:
            res += (self.helper(n, roman[::-1][d:d+3]))
            d += 2

        return res

    def helper(self, num, roman):
        one = roman[2]
        five = roman[1]
        ten = roman[0]
        if num == 0:
            return ''
        if num <= 3:
            return one*(num)
        if num == 4:
            return one+five
        if num >= 5 and num <= 8:
            return five+(one*(num%5))
        if num == 9:
            return one+ten
