# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []

        def helper(node):
            if node.left:
                helper(node.left)
            self.arr.append(node.val)
            if node.right:
                helper(node.right)

        helper(root)
        # print(self.arr)
        self.cur = 0
        
    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.arr[self.cur-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.arr)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()