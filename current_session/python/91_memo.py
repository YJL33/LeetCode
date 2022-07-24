from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def helper(idx, s):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s)-1:
                return 1
            
            ans = helper(idx+1, s)
            if int(s[idx:idx+2]) <= 26:
                ans += helper(idx+2, s)
            return ans
        
        return helper(0, s)

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
