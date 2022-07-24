import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        # use a counter
        # keep update the counter until the length is more than k
        # use sliding window
        # extend r until seen distinct characters > k
        # update the max length, (carefully handle r)
        # shrink l until seen distinct characters <= k
        
        counter = collections.Counter()
        l, r = 0, 0
        max_seen = 0
        
        while r < len(s):
            
            # extend r
            while r < len(s) and len(counter) <= k:
                # print('r, counter', r, counter)
                counter[s[r]] += 1
                r += 1
                
            # now either r == len(s) or len(counter) > k
            # l is valid here, simply update the max substr
            max_seen = max(max_seen, r-1-l)
            # print('max', max_seen)
            
            # shrink l
            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1

        max_seen = max(max_seen, r-l)
        return max_seen
        