class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # longest substring that contains at most 2 distinct chars
        # naive approach: try all i, j of s[i:j], time complexity: O(n^3)
        # sliding window: increase R until criteria is met, increase L until criteria is un-met
        charDict = {}
        l, r = 0, 0
        maxLen = 0
        while r < len(s):
            if len(charDict) <= 2:              # if <= 2, just increase r and update dict
                charDict[s[r]] = r
                r += 1
            if len(charDict) > 2:               # don't let it bigger than 2
                minL = len(s)
                for v in charDict.values():     # remove the one showed up closest to left
                    minL = min(minL, v)
                del charDict[s[minL]]
                l = minL+1

            maxLen = max(maxLen, r-l)           # keep update maxLen
        
        return maxLen

print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccababababab"))
print(Solution().lengthOfLongestSubstringTwoDistinct("cabacababcab"))
