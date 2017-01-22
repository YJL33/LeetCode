"""
 140. Word Break II

    Total Accepted: 69417
    Total Submissions: 324343
    Difficulty: Hard
    Contributors: Admin

Given a string s and a dictionary of words dict,
add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict) if self.isBreakable(s, wordDict) else []

    def isBreakable(self, s, wordDict):
        # check whether this string is breakable or not, which avoided TLE!
        if not s or not wordDict: return False
        ok = [True]
        for i in xrange(1, len(s)+1):
            ok += any(ok[j] and (s[j:i] in wordDict) for j in xrange(i)),
        return ok[-1]

    def dfs(self, s, wordDict):
        res = []                            # DFS
        for i in xrange(1,len(s)):
            if s[:i] in wordDict:
                rest = self.dfs(s[i:], wordDict)
                if rest:
                    for sub in rest:
                        res += s[:i] + ' ' + sub,
        if s in wordDict: res += s,
        return res
