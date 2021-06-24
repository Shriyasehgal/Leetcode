'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q == None:
            return True
        if (p==None) != (q==None):
            return False
        if p.val==q.val:
            cond1= self.isSameTree(p.left,q.left)
            if cond1==False: 
                return False
            cond2= self.isSameTree(p.right,q.right)
            return cond2
        return False
        
        
        
