# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        encode = ''
        def helper(root):
            nonlocal encode
            if root == None:
                return ''
            encode = str(root.val)
            if root.left:
                encode += '.' + helper(root.left)
            if root.right:
                encode += '.' + helper(root.right)
            return encode
            
        return helper(root)
            
            
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return []
        data = data.split('.')
        data = [int(x) for x in data][::-1]
        root = None
        def preOrder( lower, upper):
            if not data: return
            if lower < data[-1] and data[-1] < upper:
                val = data.pop()
                newNode = TreeNode(val)
                newNode.left = preOrder(lower,val)
                newNode.right = preOrder(val,upper)
                return newNode
        return preOrder(-float('inf'), float('inf'))
        
                
    
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans