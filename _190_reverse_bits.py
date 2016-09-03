"""
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example,
given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #int('11111111111111111111111111111111', 2) = 4294967295
        #print '{0:032b}'.format(n),
        countdown, res = 32, 0
        while countdown:
            res, n, countdown = (res<<1)+(n%2), n>>1, countdown-1
        #print '{0:032b}'.format(res)
        return res

    def reverseBits2(self, n):
        # more pythonic way
        s = '{0:032b}'.format(n)
        return int(s[::-1], 2)