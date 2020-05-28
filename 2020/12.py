"""
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. 
Input is guaranteed to be within the range from 1 to 3999.


Accepted 343.6K
Submissions 631.9K
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # given the input is 1-3999, directly check from the biggest symbol
        # by observation:
        # I, II, III, IV, V, VI, VII, VIII, IX, X
        # the rule is the same for [1-3], [4,9], [6-8], [5,10], 

        res = []
        div = 1000

        romanDict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        while div != 0:
            # print "num: ", num, " div: ", div, " res: ", res
            if (num//div) == 4:
                res += romanDict[div] + romanDict[5*div]
            elif (num//div) == 9:
                res += romanDict[div] + romanDict[10*div]
            elif (num//div) < 5:
                res += (num//div) * romanDict[div]
            else:
                res += romanDict[5*div] + ((num//div) - 5)*romanDict[div]

            num = num%div
            div = div/10

        return "".join(res)

print Solution().intToRoman(3)
print Solution().intToRoman(4)
print Solution().intToRoman(5)
print Solution().intToRoman(22)
print Solution().intToRoman(58)
print Solution().intToRoman(3999)
print Solution().intToRoman(1)
