class Solution:
    def countSubstrings(self, s: str) -> int:
        # naive approach
        # check all existing i, j -> time complexity: O(n^3)
        
        # use DP
        # if substr[i-1:j] is palindrome and s[i] == s[j]
        # dp[i][j] = true = dp[i-1][j]
        # check for odd and even substring
        # time complexity: O(n^2)

        dp = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        offset = 0
        for i in range(len(s)+1):
            dp[i][i] = True
            offset += 1

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)+1):
                if j == i+1:
                    dp[i][j] = True
                else:
                    if s[i] == s[j-1]:
                        dp[i][j] = dp[i+1][j-1]
        # print(sum([sum(r) for r in dp]))
        return sum([sum(r) for r in dp])-offset

print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))