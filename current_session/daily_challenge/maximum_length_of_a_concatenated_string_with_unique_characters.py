# naive approach:
# give all solutions and return the length longest one
# time analysis: O(2^L)

# use DP
# dp[i] = solution of arr[:i]
# say y = arr[i]
# dp[i+1] = [x.union(y) for x in dp[i]]

from typing import List
import collections
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = collections.defaultdict(list)      # dp[i] = solution of arr[:i]
        dp[0] = [set("")]

        for i in range(len(arr)):               # check the union of p and q
            p = set([c for c in arr[i]])
            if len(p) != len(arr[i]):
                dp[i+1] = dp[i]
                continue

            for q in dp[i]:
                dp[i+1].append(q)
                if len(p.intersection(q)) == 0:
                    dp[i+1].append(p.union(q))
            
        maxLen = 0
        for v in dp[len(arr)]:
            maxLen = max(maxLen, len(v))

        return maxLen

print(Solution().maxLength(["un","iq","ue"]))
print(Solution().maxLength(["cha","r","act","ers"]))
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(Solution().maxLength(["a", "abc", "d", "de", "def"]))