"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        status = [0 for l in s]

        for i in xrange(0, len(s)):
            if set(s[i]).issubset('0'):
                status[i] = 0
            elif set(s[i]).issubset(['1']):
                status[i] = 1
            elif set(s[i]).issubset(['2']):
                status[i] = 2
            elif set(s[i]).issubset(['3','4','5','6']):
                status[i] = 3
            elif set(s[i]).issubset(['7','8','9']):
                status[i] = 4
        
        #print status
        
        res = [0]
        for i in xrange(len(status)):
            if status[i] == 0:
                res[-1] -= 1
                res += 0,
            if status[i] == 1 or status[i] == 2:
                res[-1] += 1
            elif i>= 1 and ((status[i-1] == 1) or (status[i-1] ==2 and status[i] == 3)):
                res[-1] += 1
                res += 0,
            elif i>= 1 and status[i-1] == 2 and status[i] == 4:
                res += 0,

        #print res

        def F(n):
            if n == 0: return 0
            elif n == 1: return 1
            else: return F(n-1)+F(n-2)

        ans = 1
        for n in res:
            if n:
                ans *= F(n+1)
        
        return ans