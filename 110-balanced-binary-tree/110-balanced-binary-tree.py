# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root == None:
                return [True, 0]
            leftVal = helper(root.left)
            rightVal = helper(root.right)
            balanced = leftVal[0] and rightVal[0] and abs(leftVal[1]-rightVal[1]) <=1 
            return (balanced, max(leftVal[1],rightVal[1])+1)
        return helper(root)[0]