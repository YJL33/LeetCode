"""
 301. Remove Invalid Parentheses

    Total Accepted: 27724
    Total Submissions: 80517
    Difficulty: Hard
    Contributors: Admin

Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # check not-needed ')' first
        res = []
        self.helper(res, s, '(', ')')
        return res or [""]

    def helper(self, ans, inp, l, r, rev=False, last=-1):
        # print "inp: ", inp
        stk, j = 0, last+1
        for i in xrange(len(inp)):
            if inp[i] == l: stk += 1
            elif inp[i] == r: stk -= 1
            if stk >= 0: continue
            # Now we have one not-needed right, pick-out right from each consecutive rights.
            while j <= i:
                if inp[j] == r and (j == 0 or inp[j-1] != r):  # rmv 1st of consecutives
                    # print i, j
                    self.helper(ans, inp[:j]+inp[j+1:], l, r, rev, j-1)
                j += 1
            return
        # Below this line: all non-needed right are removed, reverse string and vice versa.
        backward = inp[::-1]
        # print "rev: tmp, bk => ", temp, backward
        if not rev:
            self.helper(ans, backward, ')', '(', True)
        else:
            ans += backward,