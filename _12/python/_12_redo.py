"""
 12. Integer to Roman

    Total Accepted: 92222
    Total Submissions: 214117
    Difficulty: Medium
    Contributors: Admin

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # print "input: ", num, '\n'
        worddict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 5000:"Q"}
        # roman = ['I','V','X','L','C','D','M','quinque_milia','decem_milia']
        res, div = [], 1000
        while div != 0:
            if (num//div) == 4:
                res += worddict[div] + worddict[5*div]
            elif (num//div) == 9:
                res += worddict[div] + worddict[10*div]
            elif (num//div) >= 5:
                res += worddict[5*div] + worddict[div]*((num//div)-5)
            elif (num//div) != 0:
                res += worddict[div]*(num//div)
            num = num%div
            div /= 10


        return ''.join(res)

def main():
    print Solution().intToRoman(488)
    print Solution().intToRoman(300)
    print Solution().intToRoman(737)
    print Solution().intToRoman(1024)

if __name__ == '__main__':
    main()
