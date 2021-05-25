"""
see https://leetcode.com/problems/word-break-ii/
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return [" ".join(x) for x in (self.dfs(s, wordDict, {}))]

    def dfs(self, s, wd, tmp):
        if s in tmp:
            return tmp[s]
        res = []
        if not s:
            return [[]]
        for w in wd:
            if s[:len(w)] == w:
                # print("??", w, res, tmp)
                sublist = self.dfs(s[len(w):], wd, tmp)     # consists of solutions of s[len(w):]
                for sub in sublist:
                    if sub:
                        ans = [w] + sub         # add matched word in front of sub
                        res += ans,
                    else:
                        res += [w],
                # print("res now", res)
        tmp[s] = res
        return res

    def wordBreak_TLE(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # naive approach (TLE)
        dp = [[] for _ in s]
        # O(L*N)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i:i+len(w)]:
                    dp[i] += w,
        # print(dp)
        stack = []
        for x in dp[0]:
            stack += [(0, x)],
        # print(stack)
        res = []

        # O()
        while stack:
            path = stack.pop()
            i, w = path[-1][0], path[-1][1]
            # print(i, w)
            if i+len(w) == len(s):
                res += " ".join([x[-1] for x in path]),
            elif i+len(w) < len(s):
                if dp[i+len(w)]:
                    # print dp[i+len(w)]
                    for x in dp[i+len(w)]:
                        tmp = path + [(i+len(w), x)]
                        stack += tmp,
        # print res
        return res


print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))