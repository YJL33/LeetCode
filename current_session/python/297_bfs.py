# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize_bfs(self, root):
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

            dq.append(node.left if node.left else TreeNode(float('inf')))
            dq.append(node.right if node.right else TreeNode(float('inf')))
        
        return ','.join(res)

    def deserialize_bfs(self, data):
        if data[i] == "#": return
        vals = data.split(',')

        root = TreeNode(vals[0])
        i = 1
        layer = collections.deque()
        layer.append(root)

        while layer:
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