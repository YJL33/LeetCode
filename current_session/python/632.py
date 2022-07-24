import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # simulation
        # use a heap
        # collect smallest element from k lists
        # while collecting, keep update the min-max: min=heap[0], max=current val
        # check the range when we've collected from all k (try to minimize as well)
        # overall time complexity: O(Nklogk)
        
        # 1. concatenate all lists into one
        A = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                A.append([nums[i][j], i])
        
        A.sort()                                        # O(NlogN)
        
        # 2. add all of them into heap, and keep update its count
        hp = []
        cnt = [0 for _ in range(len(nums))]
        res = [0, float('inf')]
        for val, i in A:                                # O(N)
            heapq.heappush(hp, (val,i))                 # O(logk)
            cnt[i] += 1
            while all(cnt) >= 1:                        # O(k)
                if val-hp[0][0] < res[1]-res[0]:
                    res = [hp[0][0], val]
                _, last_i = heapq.heappop(hp)           # O(logk)
                cnt[last_i] -= 1
        return res
                
                
                