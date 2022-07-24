# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # solution 1:
        # in-order traversal in advance, and get the sorted array
        # then find k closest numbers to the target in the array
        # tc: O(n) to visite whole tree, O(klogn) to find top k elements
        # sc: O(n) to store all values
        
        # solution 2:
        # keep a heap, has fixed size == k
        # do in-order traversal until there's no more updates (and the heap size == k) in the heap
        # tc: O(nlogk), worst case O(nlogn)
        # sc: O(k), worst case O(n)
        
        import heapq as hq
        
        hp = []
        
        # in-order traversal
        def helper(node):
            nonlocal hp
            if not node: return
            helper(node.left)
            
            # heap operation
            diff = abs(node.val-target)
            if len(hp) == k and diff > -1*hp[0][0]: return
            hq.heappush(hp, (-diff, node.val) )
            if len(hp) > k: hq.heappop(hp)
            
            helper(node.right)
            return
        
        helper(root)
        
        return [h[1] for h in hp]
        
        