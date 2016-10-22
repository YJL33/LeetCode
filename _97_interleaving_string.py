"""
 97. Interleaving String

    Total Accepted: 58983
    Total Submissions: 249857
    Difficultc2: Hard
    Contributors: Admin

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtc2pe: bool
        """
        # dfs
        # for each element in s3, determine which bucket it can go.
        if len(s1)+len(s2) != len(s3): return False

        l1, l2, l3, c1, c2 = len(s1), len(s2), len(s3), 0, 0
        stack, visited = [(0, 0)], set((0, 0))

        while stack:
            c1, c2 = stack.pop()
            if c1+c2 == l3:
                return True
            if c1 < l1 and s1[c1] == s3[c1+c2] and (c1+1, c2) not in visited:
                stack.append((c1+1, c2)); visited.add((c1+1, c2))
            if c2 < l2 and s2[c2] == s3[c1+c2] and (c1, c2+1) not in visited:
                stack.append((c1, c2+1)); visited.add((c1, c2+1))
        return False

    def isInterleave2(self, s1, s2, s3):
        # DP, O(m*n) space
        if len(s1)+len(s2) != len(s3): return False

        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = [[True for _ in xrange(l2+1)] for _ in xrange(l1+1)]
        for i in xrange(1, l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in xrange(1, l2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]