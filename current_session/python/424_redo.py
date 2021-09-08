# use DP(?)
# scan through whole String
# dp[i] = solution of s[:i]
# replaced[i] = [j], where j = array of replaced
# dp[i+1] = max(dp[i], replace s[i])
# ... hard to check which character

# use counter
# scan through whole String, count each character
# using sliding window and update maxLen for each i: (as right)
# extend right => check if current window is still changable within k
# if not, move left

import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # character counter within the window
        counter = collections.Counter()
        maxLen, l = 0, 0

        for r in range(len(s)):
            counter[s[r]] += 1
            # print('counter:', counter)
            baseCnt = counter.most_common(1)[0][1]
            # print('basecnt:', baseCnt)
            # update the window size
            while baseCnt and r-l+1 > baseCnt+k:
                # print('l:', l, 'r:', r)
                counter[s[l]] -= 1
                l += 1
                baseCnt = counter.most_common(1)[0][1]
            # update the max length
            maxLen = max(maxLen, r-l+1)
            # print('maxLen:', maxLen)

        return maxLen