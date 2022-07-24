# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                res.append("#")
            return
        helper(root)
        return " ".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = iter(data.split())

        def helper():
            val = next(vals)
            if val == "#": return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        return helper()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans