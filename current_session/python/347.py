"""
see https://leetcode.com/problems/top-k-frequent-elements/
"""
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nd = collections.defaultdict(int)
        for n in nums:
            nd[n] += 1

        cnts = sorted(nd.items(), key=self.getVal, reverse=True)
        # print(cnts)
        return [a[0] for a in cnts[:k]]

    def getVal(self, item):
        return item[1]

    def topKFrequent_lib(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nd = collections.Counter(nums)
        return [a[0] for a in nd.most_common(k)]

print(Solution().topKFrequent_lib([1,1,1,2,2,3], 2) == Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent_lib([4,1,-1,2,-1,2,3],2) == Solution().topKFrequent([4,1,-1,2,-1,2,3],2))