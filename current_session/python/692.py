"""
see https://leetcode.com/problems/top-k-frequent-words/
"""
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # use heap
        h = []
        wd = {}

        for w in words:
            if w in wd:
                wd[w] += 1
            else:
                wd[w] = 1

        for w in wd.keys():
            heapq.heappush(h, ((-1)*wd[w], w))

        res = []
        while k>0:
            res += heapq.heappop(h)[1],
            k -= 1

        return res

print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))