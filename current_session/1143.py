"""
1143
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]

print(Solution().longestCommonSubsequence('abcde','ace'),'is 3')
print(Solution().longestCommonSubsequence('abc','abc'),'is 3')
print(Solution().longestCommonSubsequence('abc','def'),'is 0')
print(Solution().longestCommonSubsequence("ezupkr","ubmrapg"),'is 2')
print(Solution().longestCommonSubsequence("abcba","abcbcba"),'is 5')
print(Solution().longestCommonSubsequence("oxcpqrsvwf","shmtulqrypypppp"),'is 2')
print(Solution().longestCommonSubsequence("abcba","abcbcba"), 'is 5')
print(Solution().longestCommonSubsequence("kvwrkharmnqpwxyhejgvybifmncdorglsfqlidupyvcnypwvglormj","irmdqnwnelyturkdobypezwvonqpubedetansrkjgzyzgpuxajgdaji"),'is 15')
print(Solution().longestCommonSubsequence("lmrejgzsbqpkdonytkbknstsxifofmrktcpq","hklcrebcjipetgnmlqvijovmlgripwratarmt"),'is 12')
print(Solution().longestCommonSubsequence("fcvqfcnglshwpgxujwrylqzejmdubkxs","bctsfwdelkdqzshupmrufyxklsjurevip"),'is 11')
print(Solution().longestCommonSubsequence("tufgfqlspqpidwrmjexifslkzobcjqvwlevghglynojchkvufqnwxixqnercbabm","xuhadmbsbabqzirgrcxazcxypmjebgxyzmlepcdezwbsjkjalgdotcjavojehsvax"),'is 20')

