"""
1029
"""
from typing import List
import heapq
class Solution:   
    # clarification
    # any restrictions on time/space complexity? (e.g. timeout/memory...)
    # upper/lower bound of costs[i]?
    # length of costs?
    # is is possible to have multiple distributions that meets the same cost? (e.g. [[1,1],[2,2]] )
    
    # sort approach
    # need to sort costs with diff of (cost_a - cost_b)
    # assume everyone goes to city A, then pick n people to city B which can save most money
    # python has lambda syntax, (e.g. lambda x, y = x-y), using timsort (hybrid with insertion+mergesort)
    # time complexity: timsort avg case O(2Nlog2N), best case O(2N), worst case O(2Nlog2N)
    # space complexity: O(2N) for timsort with diff array (is hidden under sort lambda syntax)

    def twoCitySchedCost_sort(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1]-x[0])
        N = len(costs)//2
        ans = 0
        for i in range(N):
            ans += costs[i][1]
        for j in range(N, 2*N):
            ans += costs[j][0]
        return ans

    # heap approach
    # pick while go through the array, meanwhile maintain the heap size (which is smaller than the range of sorting)
    # put (diff, index) into heap
    # time complexity: O(2N*logN), for 2N elements, each operate heap insert O(logN), heappop O(logN)
    # space complexity: O(N) for heap, diff is used in heap

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:        
        N = len(costs)//2
        hp = []
        ans = 0
        for i, c in enumerate(costs):
            cost_a, cost_b = c
            heapq.heappush(hp, cost_b-cost_a)
            ans += cost_a                       # assume everyone goes to city A
            if len(hp) > N:
                ans += heapq.heappop(hp)        # popped is the best person to city B instead of A => switch to B by adding the diff
        return ans
