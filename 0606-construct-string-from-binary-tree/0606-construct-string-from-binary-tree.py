# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = str(root.val)
        if not root.left and not root.right: return s
        
        s += '('
        s += self.tree2str(root.left) if root.left else ''
        s += ')'
        if root.right:
            s += '('
            s += self.tree2str(root.right)
            s += ')'
        return s
        