"""
1048. Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.

For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.

"""
import collections
from typing import List

class Solution(object):
    def longestStrChain_dp(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # sort the array by length
        # for each element, pick the longest chain among all possible predecessors (if exist) and +1
        # time: O(NlogN) + O(NS)
        # space: O(NS)

        words.sort(key=len)
        dp = collections.defaultdict(int)
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pre = w[:i]+w[i+1:]
                x = dp[pre]         # zero if not in dp
                dp[w] = max(dp[w], x+1)
        return max(dp.values())

    def longestStrChain_dfs(self, words: List[str]) -> int:
        # first put all words into dict
        # key: length, value: list of words
        # start to search from shortest words
        # tip: find from longest to shortest, instead of opposite
        ld = collections.defaultdict(set)
        minLen = float('inf')
        for w in words:
            ld[len(w)].add(w)
            minLen = min(minLen, len(w))
        
        self.maxCnt = 0
        self.visited = collections.defaultdict(int)

        def dfs(w, cnt):
            self.maxCnt = max(self.maxCnt, cnt)
            if w in self.visited and self.visited[w] >= cnt: return
            self.visited[w] = cnt
            # try to insert a character in the gap
            for i in range(len(w)):
                newWord = w[:i] + w[i+1:]
                if newWord != "" and newWord in ld[len(w)-1]:
                    dfs(newWord, cnt+1)
            return

        # try all words as beginning
        for w in words:
            dfs(w, 1)
        
        return self.maxCnt

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(Solution().longestStrChain(["abcd","dbqca"]))
print(Solution().longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]), 'should be 7')