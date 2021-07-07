"""
91
"""
class Solution(object):
    def numDecodings(self, s):
        # print('s', s)
        if s == '0': return 0
        self.dp=[0 for _ in range(len(s)+1)]
        self.dp[0] = 0                  # ending with s[:i]
        self.dp[1] = 1 if s[0] != '0' else 0
        
        i = 2
        prvIsZero, prevIsDD = False, False
        while i <= len(s):
            # print('?')
            if i-1 < 0 or i-1 >= len(s) or (s[i-1] == '0' and s[i-2] not in '12'): return 0
            if s[i-1] == '0':
                if prevIsDD: self.dp[i-1] = self.dp[i-2]   # correction
                self.dp[i] = self.dp[i-1]
                prvIsZero, prevIsDD = True, False
            else:
                # print('?',int(s[i-1:i+1]))
                if 10 <= int(s[i-2:i]) <= 26 and not prvIsZero:
                    self.dp[i] += max(self.dp[i-1], 1) + max(self.dp[i-2], 1)
                    prevIsDD = True
                else:
                    self.dp[i] = self.dp[i-1]
                    prevIsDD = False
                prvIsZero = False
            if self.dp[i] == self.dp[i-1] == 0: return 0
            i += 1
            # print("dp:",self.dp)

        return self.dp[-1]

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
