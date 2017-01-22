"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = []
        for c in s:
            if c in roman:
                res.append(roman[c])
            else:
                print "unable to identify given roman numeral"
                return

        tot = 0
        for i in xrange(len(res)):
            if i+1 == len(res):
                tot += res[i]
            elif res[i+1] > res[i]:
                tot -= res[i]
            else:
                tot += res[i]

        return tot