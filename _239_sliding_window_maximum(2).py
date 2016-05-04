"""
239. Sliding Window Maximum

Given an array nums,
A sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements that need to be considered.
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # A faster solution beats 93.78 percent
        # Here we use ans[i-k] to replace all ans[-1], the speed is increased.

        if len(nums) == 0: return []            # Special cases

        ans = [max(nums[0:k])]                  # initialize the answer
        for i in range(k,len(nums)):            # for each latest element:
            if nums[i] >= ans[i-k]:             # if latest element is max ...
                ans.append(nums[i])             # ... add it
            elif nums[i-k] == ans[i-k]:         # if oldest element is max ...
                ans.append(max(nums[i-k+1:i+1]))# ... find a new max
            else:                               # if neither ...
                ans.append(ans[i-k])            # ... just add max again

        return ans
