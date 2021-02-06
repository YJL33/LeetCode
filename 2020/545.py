# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        lb = [root.val]
        if root.left is not None:
            cur = root.left
            while cur is not None:
                lb += cur.val,
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur = cur.right
            lb.pop()
        rb = []
        if root.right is not None:
            cur = root.right
            while cur is not None:
                rb += cur.val,
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur = cur.left
            rb.pop()
        rb.reverse()

        leaves = []
        def dfs(node):
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
        
        dfs(root)
        # print lb
        # print leaves
        # print rb
        return lb+leaves+rb