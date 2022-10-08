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
        res = ''
        if root == None: return res
        res+=(str(root.val)+'.')
        res+=self.serialize(root.left) 
        res+=self.serialize(root.right)
        return res
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data[:-1]
        if data == '': return None
        
        data = deque([int(i) for i in data.split('.')])
        
        
        def helper(lower,upper):
            
            if data and data[0] > lower and data[0] < upper:
                val = data.popleft()
                newNode = TreeNode(val)
                newNode.left = helper(lower,val)
                newNode.right = helper(val,upper)
            else:
                return None
            return newNode
        return helper(-float('inf'),float('inf'))
        
            
        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans