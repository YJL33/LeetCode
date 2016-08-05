"""
128. Longest Consecutive Sequence

Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert nums to set => cost O(n)
        # check each element in set or not => cost O(1)*(~n) as needed
        numset = set(nums)
        res = 0
        for n in nums:
            value = n
            if (value-1) not in numset:     # cost O(1)
                count = 1
                while (value+1) in numset:  # cost O(k) (sequence length = k)
                    count += 1
                    value += 1
                res = max(count, res)       # update the maximum length

        return res