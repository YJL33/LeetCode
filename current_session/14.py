'''
14
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            cnt = 0       # count of matched character
            while cnt < min(len(prefix), len(s)):
                if prefix[cnt] == s[cnt]:
                    cnt += 1
                else:
                    break
            if cnt == 0:
                return ""
            else:
                prefix = prefix[:cnt]
        return prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
