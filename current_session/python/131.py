from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # use DP
        # start searching from backward
        # dp[0] is the solution
        dp = [[] for _ in range(len(s)+1)]
        dp[-1] = [[]]
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        return dp[0]

# print(Solution().partition("aab"))
print(Solution().partition("aabaa"))