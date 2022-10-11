# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.data = None
        
    '''def preorder(self,root):
        if root == None:
            return ''
        res = ''
        res +=(str(root.val) + '.')
        res += self.preorder(root.left)
        res += self.preorder(root.right)
        return res
    def inorder(self,root):
        if root == None:
            return ''
        res = ''
        res += self.inorder(root.left)
        res +=(str(root.val) + '.')
        res += self.inorder(root.right)
        return res'''
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''pre = self.preorder(root)
        ino = self.inorder(root)
        return pre[:-1] + '#' + ino[:-1]'''
        if not root: return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
    '''def buildTree(self, pre, ino):
        if not pre: return None
        val = pre[0]
        idx = ino.index(val)
        node = TreeNode(int(val))
        node.left = self.buildTree(pre[1:idx+1],ino[0:idx])
        node.right = self.buildTree(pre[idx+1:],ino[idx+1:])
        return node'''
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if type(data) == str:
            data = data.split(',')
            
        self.data = data
        if self.data[0] == 'x': return None
        node = TreeNode(int(self.data[0]))
        node.left = self.deserialize(self.data[1:])
        node.right = self.deserialize(self.data[1:])
        return node
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))