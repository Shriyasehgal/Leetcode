# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return 'x'
        return ','.join([str(root.val),self.serialize(root.left),self.serialize(root.right)])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')[::-1]
        def helper():
            if not data: return None
            val = data.pop()
            if val == 'x':
                return None
            root = TreeNode(val)
            root.left = helper()
            root.right = helper()
            return root
        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))