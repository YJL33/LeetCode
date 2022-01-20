from typing import List
import collections
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # use DP
        counter = {k:v for k, v in collections.Counter(s).items() if v >= 2}
        if not counter: return 0
        L = len(s)
        k = 1           # length of substring

        while k < L:
            tmp = collections.Counter()
            for i in range(L-k+1):          # possible starts
                end_index = i+k
                substr = s[i:end_index+1]
                if (substr[:-1] in counter) or substr in tmp:
                    tmp[substr] += 1
            if not tmp: break
            counter = {a:b for a, b in tmp.items() if b >= 2}
            k += 1

        return k if any([v >= 2 for _, v in counter.items()]) else k-1
            
print(Solution().longestRepeatingSubstring("abcd"))
print(Solution().longestRepeatingSubstring("abbaba"))
print(Solution().longestRepeatingSubstring("aabcaabdaab"))
print(Solution().longestRepeatingSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), '== 63')
