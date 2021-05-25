import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # keep a element counter, and put a tuple (cnt, element) into a heap

        nd = {}
        mh = []

        for n in nums:
            if n in nd:
                nd[n] += 1
            else:
                nd[n] = 1
        
        for n in nd.keys():
            heapq.heappush(mh, ((-1)*nd[n], n))

        res = []
        while k > 0:
            res.append(heapq.heappop(mh)[1])
            k -= 1

        return res