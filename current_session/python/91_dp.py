class Solution:
    
    # DP bottom-up
    # tc: O(n)
    # sc: O(n), can be optimized into O(1)

    def numDecodings(self, s: str) -> int:
        # dp[i] is the solution of s[:i]
        # check s[i-1] is valid single digit or s[i-2:i] is valid double digit
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1

        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2,len(dp)):

            # Check if successful single digit decode is possible.
            if s[i-1] != '0':
                dp[i] = dp[i-1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[len(s)]

print(Solution().numDecodings("12"), 'should be 2')
print(Solution().numDecodings("012"), 'should be 0')
print(Solution().numDecodings("123"), 'should be 3')
print(Solution().numDecodings("39584736"), 'should be 1')
print(Solution().numDecodings("1938192377104101929381292011192931012"),'should be 320')
print(Solution().numDecodings("1938192377104101929381292011192930012"), 'should be 0')
print(Solution().numDecodings("230"), 'is 0')
print(Solution().numDecodings("10"),'is 1')
print(Solution().numDecodings("0"),'is 0')
print(Solution().numDecodings("06"),'is 0')
print(Solution().numDecodings("004123453243"),'is 0')
print(Solution().numDecodings("2101"),'is 1')
print(Solution().numDecodings("2611055971756562"),'is 4')