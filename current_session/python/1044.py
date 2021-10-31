import collections
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        # use dict
        def hasDuplicate(m):
            # print('has dupe?', m)
            if m == 0 or m == len(s): return False
            lenDict = collections.defaultdict(int)
            lenDict[s[:m]] = 0
            for i in range(1,len(s)-m+1):
                if s[i:i+m] in lenDict:
                    # print('got it:', lenDict[s[i:i+m]], 'index:', i)
                    return lenDict[s[i:i+m]]
                lenDict[s[i:i+m]] = i
            return -1

        # use binary search
        # we want to find m such that
        # hasDuplicate(m) == True
        # hasDuplicate(m+1) == False
        l, r = 0, len(s)
        while l < r:
            m = (r+l)//2
            if hasDuplicate(m) == -1:     # use smaller m
                r = m
            else:
                l = m+1
        # termination criteria: l == r
        x = hasDuplicate(l-1)
        return s[x:x+l-1] if x != -1 else ""

# print(Solution().longestDupSubstring("banana"))
# print(Solution().longestDupSubstring("abcd"))
# print(Solution().longestDupSubstring("abcdefghijklmnopqabcdepaqcidhgmckdowld;aicmdksiaoemghinbhggausydtfa"))
print(Solution().longestDupSubstring("aa"))
print(Solution().longestDupSubstring("aaa"))