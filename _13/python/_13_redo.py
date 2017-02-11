"""
 13. Roman to Integer

    Total Accepted: 127887
    Total Submissions: 291602
    Difficulty: Easy
    Contributors: Admin

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numdict, res = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}, 0
        for i, c in enumerate(s):
            if (i+1) < len(s) and numdict[c] < numdict[s[i+1]]:
                res += -(numdict[c])
            else:
                res += numdict[c] 
        return res

def main():
    print Solution().romanToInt("DCXXI")
    print Solution().romanToInt("MMMCMXCIX")
    print Solution().romanToInt("III")
    print Solution().romanToInt("DCVIII")
    print Solution().romanToInt("MDCXXIV")

if __name__ == "__main__":
    main()