# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if root == None:
                return 0
            maxLeft = helper(root.left)
            maxRight = helper(root.right)
            res = max(res, maxLeft+maxRight)
            return max(maxLeft,maxRight)+1
        helper(root)
        return res
        
        