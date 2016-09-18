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
        tmp, dgt = n, 0             # it's a "dgd"-digit number
        while tmp > 0:
            tmp -= (dgt+1)*9*(10**dgt)
            dgt += 1

        dgt -= 1
        cnt, start, startpos = 0, 10**(dgt), 0
        while cnt < dgt:
            startpos += (cnt+1)*9*(10**cnt)
            cnt += 1

        print "n", n, " =>", dgt+1, start, startpos
        tgt = ((n-startpos)/(dgt+1))+start
        rmd = (n-startpos)%(dgt+1)
        print tgt, rmd
        if rmd == 0: tgt -= 1
        return int(str(tgt)[rmd-1])
