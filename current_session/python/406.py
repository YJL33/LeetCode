from sortedcontainers import SortedList
from typing import List
class Solution:
    def reconstructQueue_sl(self, people: List[List[int]]) -> List[List[int]]:
        # opposite way of top-voted solution
        # prepare all un-assigned indices in a sorted list (unassigned_idx)
        # sort the people with height, now shortest person will come at first
        # assign person (following sorting order):
        # the first (shortest) person will have its p[1] index in the sorted list
        # e.g. j = unassigned_idx[p[1]], ans[j] = p[0]
        # after assignment, remove the index from sorted list
        #
        # analysis: (given n people)
        # tc: O(nlogn) for sorting, O(nlogn) to assign each one into output array
        # sc: O(n) for output array
        
        people.sort(key=lambda p: (p[0], -p[1]))        # use -p[1] to avoid people in the same heights are interferreing each other
        unassigned_idx = SortedList([i for i in range(len(people))])
        ans = [None for _ in range(len(people))]
        for h, idx in people:
            j = unassigned_idx[idx]
            ans[j] = [h,idx]
            unassigned_idx.pop(idx)

        return ans

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people from tall to short
        # insert from tall to short
        # tc: O(nlogn) for sorting, O(n)*X for insertion, where X is the time complexity of each insert, best case O(1) worst case O(n)
        # sc: O(n) for output array
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))