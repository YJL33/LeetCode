"""
43. Multiply Strings

Given two numbers represented as strings,
return multiplication of the numbers as a string.

Note:

    The numbers can be arbitrarily large and are non-negative.
    Converting the input string to integer is NOT allowed.
    You should NOT use internal library such as BigInteger.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # implement the process of multiply on paper (by hand)
        # e.g.  125   <- num2
        #      x 12   <- num1
        #  --------
        #       250
        #      125
        #  --------
        #      1500
        carry, multi, shift, pos = 0, 0, 0, 0
        res = {}

        for a in num1[::-1]:
            pos, carry = 0, 0
            for b in num2[::-1]:
                multi, carry = (int(a)*int(b)+carry)%10, (int(a)*int(b)+carry)//10
                #print "what's going on?", a,b, (int(a)*int(b)+carry), multi, carry
                if pos+shift in res:
                    res[pos+shift] += multi,
                else:
                    res[pos+shift] = [multi]
                pos += 1
            if carry: res[pos+shift] = [carry]
            shift += 1

        #print res
        carry, sumup, zeroes = 0, '', 0
        for k in xrange(len(res)):
            temp = sum(res[k]) + carry
            multi, carry = temp%10, temp/10
            if k == 0 or multi != 0:
                sumup = str(multi) + "0"*zeroes + sumup
                zeroes = 0
            else:
                zeroes += 1
        if carry:
            sumup = str(carry) + "0"*zeroes + sumup
        
        return sumup
