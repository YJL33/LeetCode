# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# post-order traverse
class Codec:

    def serialize(self, root):
        self.res = []
        def post_order_serialize(node):
            if not node:
                self.res.append("#")
                return
            post_order_serialize(node.left)
            post_order_serialize(node.right)
            self.res.append(str(node.val))
            return
        
        post_order_serialize(root)
        return ",".join(self.res)

    def deserialize(self, data):

        vals = data.split(",")
        self.idx = len(vals)-1
        def post_order_deserialize():       # construct in a reversed way: root-right-left
            if self.idx < 0:
                return None
            self.idx -= 1                   # minus 1 no matter the node is null or not
            if vals[self.idx+1] == "#":     # no need to go deeper, simply return None
                return None
            node = TreeNode(int(vals[self.idx+1]))
            node.right = post_order_deserialize()
            node.left = post_order_deserialize()
            
            return node

        return post_order_deserialize()
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

print(ser.serialize(deser.deserialize("#,#,2,#,#,4,#,#,5,3,1")) == "#,#,2,#,#,4,#,#,5,3,1" )
print(ser.serialize(deser.deserialize("#,#,1,#,2,#,#,4,3,#,#,6,#,#,10,#,#,15,13,7,5")) == "#,#,1,#,2,#,#,4,3,#,#,6,#,#,10,#,#,15,13,7,5" )