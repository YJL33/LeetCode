"""
see https://leetcode.com/problems/make-the-string-great/
"""
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: return s

        # brute force
        res = s
        checker = True

        while checker:
            checker = False
            # iterate through the string
            for i in xrange(len(res)-1):
                if abs(ord(res[i]) - ord(res[i+1])) == 32:
                    res = res[:i] + res[i+2:]       # update the answer
                    checker = True
                    break

        return res


print Solution().makeGood("leeEetcode")
print Solution().makeGood("leeEetcodeeE")
print Solution().makeGood("abBAcC")
print Solution().makeGood("aA")
print Solution().makeGood("s")
print Solution().makeGood("mC")
