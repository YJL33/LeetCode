from typing import List
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # use a sliding window
        # count the number of ones first
        # keep a window with fixed size and move from left to right, and update the required moves
        # best case: [1,1,1,1,...1] (all one)
        # worst case: [1,1,1,1,...1] (all zero)
        count, window = sum(data), sum(data[:count])
        min_seen = count - window
        l, r = 0, count
        while r < len(data):
            window += data[r]-data[l]
            min_seen = min(min_seen, count-window)
            l, r = l+1, r+1
        return min_seen
