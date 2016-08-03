"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≦ k ≦ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import heapify, heappop

        # Use a dictionary to record all numbers => O(n)
        dct = {}
        for n in nums:
            if n in dct:
                dct[n] += 1
            else:
                dct[n] = 1

        # Extract the key value pair out of dictionary => O(n)
        res = []
        for key, value in dct.iteritems():
            res.append((value, key))
            
        # Heapify the list => O(logn)
        heapq.heapify(res)

        # Get the top K items => O(1)*k
        return [x[1] for x in heapq.nlargest(k, res)]