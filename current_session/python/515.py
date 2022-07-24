# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # use bfs
        if not root: return []
        layer = [root]
        res = []
        while layer:
            tmp = []
            mx = float('-inf')
            for node in layer:
                mx = max(mx, node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            layer = tmp
            res.append(mx)
        return res
