'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.helperBST(root, -sys.maxint , sys.maxint):
            return  True
        return False
    
    def helperBST(self, root, mini, maxx):
        if root== None:
            return True
        
        if root.val<mini or root.val>maxx:
            return False
        
        if self.helperBST(root.left, mini, root.val-1) and self.helperBST(root.right, root.val+1,maxx):
            return True
