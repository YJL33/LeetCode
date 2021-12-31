# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional, List
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # find critical point: local maxima or local minima
        # minDist, maxDist
        prev = None
        cur = head
        i = 0
        res = []
        minSeen = float('inf')
        while cur:
            if prev and cur.val < prev.val and cur.next and cur.val < cur.next.val:     # local minima
                if res: minSeen = min(minSeen, i-res[-1])
                res.append(i)
            elif prev and cur.val > prev.val and cur.next and cur.val > cur.next.val:     # local maxima
                if res: minSeen = min(minSeen, i-res[-1])
                res.append(i)
            i += 1
            prev = cur
            cur = cur.next
        if len(res) <= 1: return [-1, -1]
        return [minSeen, res[-1]-res[0]]


