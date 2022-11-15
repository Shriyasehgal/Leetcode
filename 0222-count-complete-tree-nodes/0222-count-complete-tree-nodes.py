# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftLevel = self.countLeft(root)
        rightLevel = self.countRight(root)
        if leftLevel == rightLevel:
            return 2**rightLevel - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
    def countLeft(self, root):
        level = 1
        while root.left:
            root = root.left
            level +=1
        return level
    def countRight(self,root):
        level = 1
        while root.right:
            root = root.right
            level+=1
        return level
        
                
                
        