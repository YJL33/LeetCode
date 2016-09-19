"""
 400. Nth Digit

    User Accepted: 53
    User Tried: 148
    Total Accepted: 56
    Total Submissions: 282
    Difficulty: Easy

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9: return n
        startpos, tmp, dgt = 0, n, 0             # it's a "dgt"-digit number
        while tmp > 0:
            span = (dgt+1)*9*(10**dgt)
            tmp, startpos, dgt = tmp-span, startpos+span, dgt+1

        dgt -= 1
        startpos, start = startpos-span, 10**(dgt)

        tgt, rmd = ((n-startpos)/(dgt+1))+start, (n-startpos)%(dgt+1)

        return int(str(tgt)[rmd-1]) if rmd != 0 else int(str(tgt-1)[rmd-1])
