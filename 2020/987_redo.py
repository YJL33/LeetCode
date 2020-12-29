"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        pd = collections.defaultdict(list)
        def helper(node,pos,layer=0):
            if not node: return
            pd[pos].append((layer,node.val))
            helper(node.left, pos-1, layer+1)
            helper(node.right, pos+1, layer+1)
        helper(root,0)
        keys = pd.keys()
        keys.sort()

        ans = []
        for k in keys:
            nodes = pd[k]
            nodes.sort()
            ans += [n[1] for n in nodes],
        return ans
