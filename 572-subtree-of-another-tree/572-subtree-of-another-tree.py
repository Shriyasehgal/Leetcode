# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,p,q):
        if p == None and q == None:
            return True
        if p == None or q== None:
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and p.val == q.val:
            return True
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if root and root.val == subRoot.val and self.isSameTree(root,subRoot):
            return True
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True
        else:
            return False
        