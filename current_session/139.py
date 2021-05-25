"""
see https://leetcode.com/problems/word-break/
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # brute force
        # for each word, match it with the beginning substring
        # if found match, so on and so forth
        # if no match, return false
        # O(N*L), where N = number of words in wordDict, L = length of s

        # use DFS
        # O(L^2), where L is the length of s
        # optimization: we can search only with the length of words
        # O(L*k), where k is the number of lengths (e.g. k=3 for [apple, juice, banana, orange, dog, cat, car])

        wd = {}
        for w in wordDict:
            wd[w] = 1

        stack = []
        stack += 0,

        visited = [0 for _ in s]        # critical! start to search from each i and memorize whether it's visited

        while stack:
            i = stack.pop()
            if visited[i] == 0:
                for j in range(i+1, len(s)+1):
                    # print i, j, s[i:j]
                    if s[i:j] in wd:
                        if j == len(s):
                            return True
                        else:
                            stack += j,
                    # print "after", stack
                visited[i] = 1
        return False

print(Solution().wordBreak("cala", ["la", 'ca']))
print(Solution().wordBreak("cala", ["ca", 'la']))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(Solution().wordBreak("applepenapple",["apple","pen"]))
print(Solution().wordBreak("applepenapple",["apple","pen"]))
print(Solution().wordBreak("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))