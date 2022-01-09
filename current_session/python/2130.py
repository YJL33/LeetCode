# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # twin: i and n-i-1
        # get N first
        nodeDict = {}
        cur = head
        i = 0
        while cur:
            nodeDict[i] = cur.val
            cur, i = cur.next, i+1
        N = i
        j = 0
        maxSeen = float('-inf')
        while j <= (N/2)-1:
            maxSeen = max(maxSeen, nodeDict[j]+nodeDict[N-j-1])
            j += 1
        
        return maxSeen
