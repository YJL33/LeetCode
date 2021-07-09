"""
139
"""
class Solution(object):
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DP
        ws = set(wordDict)
        if s in ws: return True
        dp = [False for _ in range(len(s)+1)]       # dp[i] = True if dp[0:i] in ws
        dp[0] = True
        for end in range(len(dp)):
            for start in range(end):
                if dp[start] and s[start:end] in ws:
                    dp[end] = True
        return dp[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DFS
        ws = set(wordDict)
        if s in ws: return True
        stack = [0]
        visited = [0 for _ in s]
        
        while stack:
            i = stack.pop()
            if visited[i] == 0:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in ws:
                        if j == len(s):
                            return True
                        else:
                            stack += j,
                visited[i] = 1
        return False


print(Solution().wordBreak("cala", ["la", 'ca']))
print(Solution().wordBreak("cala", ["ca", 'la']))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(Solution().wordBreak("applepenapple",["apple","pen"]))
print(Solution().wordBreak("applepenapple",["apple","pen"]))
print(Solution().wordBreak("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))