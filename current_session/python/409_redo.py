# O(N)
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cd = collections.defaultdict(int)
        odd, res = 0, 0
        for i in range(len(s)):
            c = s[i]
            if c not in cd or cd[c]%2 == 0:
                odd += 1
            else:
                odd -= 1
                res += 2
            cd[c] += 1
        return res if odd == 0 else res+1