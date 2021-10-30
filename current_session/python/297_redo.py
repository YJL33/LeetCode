# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS
        if not root: return "#"
        dq = collections.deque()
        dq.append(root)
        res = []
        while dq:
            node = dq.popleft()
            if node.val != float('inf'):
                res.append(str(node.val))
            else:
                res.append("#")
                continue

            if node.left:
                dq.append(node.left)
            else:
                dq.append(TreeNode(float('inf')))
            if node.right:
                dq.append(node.right)
            else:
                dq.append(TreeNode(float('inf')))
        
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        if data[i] == "#": return
        vals = data.split(',')

        root = TreeNode(vals[i])
        i += 1
        layer = collections.deque()
        layer.append(root)

        while layer:
            # print('node:', layer[0].val)
            node = layer.popleft()
            if i < len(vals) and vals[i] != "#":
                x = TreeNode(vals[i])
                node.left = x
                layer.append(x)
            else:
                node.left = None
            i += 1
            if i < len(vals) and vals[i] != "#":
                y = TreeNode(vals[i])
                node.right = y
                layer.append(y)
            else:
                node.right = None
            i += 1
        
        return root

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

print(ser.serialize(deser.deserialize("1234567########")) == "1234567########" )
print(ser.serialize(deser.deserialize("1#367####")) == "1#367####" )