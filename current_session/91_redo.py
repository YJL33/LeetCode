"""
91
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0
        # use dp, from right to left
        i = len(s)-2
        while i >= 0:
            if s[i] == '0':             # can not exist alone
                i -= 1
                continue
            else:
                if int(s[i:i+2]) <= 26:
                    dp[i] = dp[i+1]+dp[i+2]
                else:
                    dp[i] = dp[i+1]
            i -= 1
        # print(dp)
        return dp[0]

print(Solution().numDecodings("12"), 'should be 2')
print(Solution().numDecodings("123"), 'should be 3')
print(Solution().numDecodings("39584736"), 'should be 1')
print(Solution().numDecodings("1938192377104101929381292011192931012"),'should be 320')
print(Solution().numDecodings("1938192377104101929381292011192930012"), 'should be 0')