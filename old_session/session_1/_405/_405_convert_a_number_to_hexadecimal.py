"""
405. Convert a Number to Hexadecimal

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, two's complement method is used.

IMPORTANT:
You must not use any method provided by the library which converts/formats the number to hex directly.
Such solution will result in disqualification of all your submissions to this problem.

Users may report such solutions after the contest ends and we reserve the right of final decision and interpretation in the case of reported solutions.

Note:

    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    The given number is guaranteed to fit within the range of a 32-bit signed integer.
    You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

Input:
26

Output:
"1a"

Example 2:

Input:
-1

Output:
"ffffffff"
"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        converthex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        res = ""

        if num == 0: return "0"

        elif num < 0:
            num += 2 ** 32

        while num: num, res = num//16, converthex[num%16]+res
        return res


    def toHex2(self, num):
        converthex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        res = ""

        if num == 0: return "0"

        elif num == -1: return "ffffffff"

        elif num > 0:
            while num: num, res = num//16, converthex[num%16]+res
            return res

        else:
            # use binary then 16-digit
            num, bin = -num-1, []
            while num:
                if num%2: bin += 1,
                else: bin += 0,
                num = num>>1

            invbin = []
            for i in bin:
                if i == 0: invbin += 1,
                else: invbin += 0,

            while len(invbin)%4: invbin += 1,

            hexres, tmp, counter = "", 0, 0
            for i in xrange(len(invbin)):
                tmp += invbin[i]<<i%4
                if i%4 == 3: hexres, tmp = converthex[tmp]+hexres, 0

            hexres = "f"*(8-len(invbin)//4) + hexres

            return hexres