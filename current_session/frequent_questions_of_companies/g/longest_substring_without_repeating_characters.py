class Solution:
    def lengthOfLongestSubstring(self, S):
        # use sliding window
        if not S: return 0
        start, end = 0, 1               # ans = S[start:end]
        charMap = {}
        charMap[S[0]] = 0
        maxLen = 1
        for i in range(1,len(S)):
            if S[i] in charMap: start = max(start,charMap[S[i]]+1)
            end = i+1
            maxLen = max(maxLen, end-start)
            charMap[S[i]] = i
        return maxLen

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring(""))