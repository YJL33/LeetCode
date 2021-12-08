from typing import List
import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # use sliding window and monotonic queue
        # keep increase R (expand the window) until the abs diff > limit
        # keep increase L (shrink the window) until the abs diff <= limit
        # incQ: monotonic decrease queue => incQ[0] is min of window
        # decQ: monotonic increase queue => decQ[0] is max of window
        # keep maintain and update the window size

        decQ, incQ = collections.deque(), collections.deque()
        l, r = 0, 0
        maxWindow = 0
        while r < len(nums):
            while incQ and nums[r] <= nums[incQ[-1]]:
                incQ.pop()
            while decQ and nums[r] >= nums[decQ[-1]]:
                decQ.pop()
            incQ.append(r)
            decQ.append(r)

            while nums[decQ[0]] - nums[incQ[0]] > limit:
                l += 1
                if l > incQ[0]: incQ.popleft()
                if l > decQ[0]: decQ.popleft()
            
            maxWindow = max(maxWindow, r-l+1)
            r += 1
        
        return maxWindow

