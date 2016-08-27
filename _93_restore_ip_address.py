"""
93. Restore IP Addresses

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ip = []
        length = len(s)
        for a in xrange(1,4):
            for b in xrange(1,4):
                for c in xrange(1,4):
                    for d in xrange(1,4):
                        if sum([a,b,c,d]) == length:
                            A, B, C, D = s[:a], s[a:a+b], s[a+b:a+b+c], s[-d:]
                            if self.helper(A) and self.helper(B) and self.helper(C) and self.helper(D):
                                ip.append(s[:a]+'.'+s[a:a+b]+'.'+s[a+b:a+b+c]+'.'+s[-d:])

        return ip

    def helper(self, A):
        # check whether this numbers is valid or not
        if A[0] == '0' and len(A) > 1:
            return False
        if int(A) > 255:
            return False
        else:
            return True
