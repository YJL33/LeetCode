from typing import List
import heapq
class Solution:
    # clarification
    # upperbound/lowerbound/type of nums[i]
    # length of nums

    # idea
    # in other word its asking diff of max and min after 3 moves

    # sort
    # try pop first3, first2+last1... last3 and check the range
    # tc: O(nlogn) + O(1)
    # sc: O(n) for original nums
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4: return 0
        nums.sort()
        l, r = 0, len(nums)-4
        min_diff = nums[r] - nums[l]
        for c in range(1, 4):
            min_diff = min(min_diff, nums[r+c]-nums[l+c])
        return min_diff
        
    # heap
    # maintain 2 heap, minHeap to store top 3 biggest elements and maxHeap to store bottom 3 (smallest) elements
    # expand those and check the diff
    # tc: O(nlogn) to craft 2 heap, sort and get the result (negligible due to size of heap)
    # sc: O(h), where h is the size of heap (negligible due to size of heap)
    def minDifference_heap(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        minH, maxH = [], []
        for n in nums:
            heapq.heappush(minH, n)
            if len(minH) > 4: heapq.heappop(minH)
            heapq.heappush(maxH, -n)
            if len(maxH) > 4: heapq.heappop(maxH)
        minH.sort()
        maxH.sort()
        return min([minH[i]+maxH[~i] for i in range(4)])