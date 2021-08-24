# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def treeToStr(node):
            if node:
                res.append(str(node.val))
                treeToStr(node.left)
                treeToStr(node.right)
            else:
                res.append("#")
            return

        res = []
        treeToStr(root)
        return " ".join(res)

    def deserialize(self, data):
        def strToTree():
            val = next(vals)
            if val == "#": return None
            node = TreeNode(int(val))
            node.left = strToTree()
            node.right = strToTree()
            return node
        
        vals = iter(data.split())
        return strToTree()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))