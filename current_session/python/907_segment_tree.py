# TLE
from typing import List
class SegmentTreeNode:
    def __init__(self, min_val, start, end, left=None, right=None):
        self.min = min_val
        self.start = start
        self.end = end          # inclusive
        self.left = left
        self.right = right
        
class MinSegmentTree:
    def __init__(self, arr):
        self.root = self._helper(arr, 0, len(arr)-1)
    
    # build segment tree from given array
    # make sure that its balanced height
    def _helper(self, arr, start, end):
        if start > end: return
        if start == end:
            return SegmentTreeNode(arr[start], start, end)
        mid = (start+end)//2
        l = self._helper(arr, start, mid)
        r = self._helper(arr, mid+1, end)
        return SegmentTreeNode(min(l.min, r.min), start, end, l, r)
    
    def query_min(self, node, s, e):
        if not node: print("s, e", s, e, "???")
        if node.start == s and node.end == e:
            return node.min
        mid = (node.start+node.end)//2
        if e <= mid:        # at left side
            return self.query_min(node.left, s, e)
        elif s > mid:
            return self.query_min(node.right, s, e)
        else:
            # print('node', node.min, node.start, node.end, 'mid=', mid)
            return min(self.query_min(node.left, s, mid), self.query_min(node.right, mid+1, e))
    
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # e.g. 3,1,2,4 -> 1,1,2 -> 1,1 -> 1
        # 2 solutions
        # sliding window (with heap)
        # 'steps' moved: O((n^2)/2), heap operation O(logW), where W is the size of window, worst case O(logn)
        # segment tree
        # initialization O(n), query: O(logn), number of queries: (n^2)/2
        # print('arr', arr)
        st = MinSegmentTree(arr)
        # print('st:', st.root.min, st.root.start, st.root.end, st.root.left.min, st.root.right.min)
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                # query
                res += st.query_min(st.root, i, j)
        return res