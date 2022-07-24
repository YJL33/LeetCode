# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# pre-order traverse
class Codec:

    def serialize(self, root):
        self.res = []
        def pre_order_serialize(node):
            if not node:
                self.res.append("#")
                return
            self.res.append(str(node.val))
            pre_order_serialize(node.left)
            pre_order_serialize(node.right)
            return
        
        pre_order_serialize(root)
        return ",".join(self.res)
        

    def deserialize(self, data):
        self.idx = 0
        vals = data.split(",")
        def pre_order_deserialize():
            if self.idx == len(vals):
                return None

            self.idx += 1                   # increment idx by 1 (no matter current node is null or not)
            if vals[self.idx-1] == "#":     # no need to go deeper, simply return None
                return None

            node = TreeNode(int(vals[self.idx-1]))
            node.left = pre_order_deserialize()
            node.right = pre_order_deserialize()
            return node

        return pre_order_deserialize()
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

print(ser.serialize(deser.deserialize("5,3,2,1,#,#,#,4,#,#,7,6,#,#,13,10,#,#,15,#,#")) == "5,3,2,1,#,#,#,4,#,#,7,6,#,#,13,10,#,#,15,#,#" )
print(ser.serialize(deser.deserialize("1,2,#,#,3,4,#,#,5,#,#")) =="1,2,#,#,3,4,#,#,5,#,#" )