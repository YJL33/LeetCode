"""
see https://leetcode.com/problems/decode-ways/
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        mem = {}

        def helper(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s)-1:
                return 1

            if index in mem:
                return mem[index]
            else:
                ans = helper(index+1)
                if int(s[index:index+2]) <= 26:
                    ans += helper(index+2)
                mem[index] = ans
                return mem[index]
        
        return helper(0)

print(Solution().numDecodings("12"))
print(Solution().numDecodings("123"))
print(Solution().numDecodings("39584736"))