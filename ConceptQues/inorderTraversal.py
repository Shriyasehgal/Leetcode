'''Given the root of a binary tree, return the inorder traversal of its nodes' values.'''
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Tree:
    def __init__(self,nodelist=[]):
        self.nodelist=nodelist
        
    def createTree(self,root,i,n):
        if i>n:
            return None
            
        if i<n:
            node=TreeNode(self.nodelist[i])
            root=node
            root.left=self.createTree(root.left,2*i+1,n)
            root.right=self.createTree(root.right,2*i+2,n)
        return root
         
class Solution(object):
  
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root != None:
            self.helper(root,res)
        return res
        
    def helper(self,root,res):
        if root.left==None and root.right== None:
            res.append(root.val)
            return res
        if root.left!=None: 
            res=self.helper(root.left,res)
            
        res.append(root.val)
        
        if root.right!= None:
            res = self.helper(root.right,res)
        return res
 
inp=input("Enter the nodes,")
inp=inp.split(',')
tree=Tree(inp)
root=tree.createTree(None,0,len(inp))
s=Solution()
s.inorderTraversal(root)

    
        
