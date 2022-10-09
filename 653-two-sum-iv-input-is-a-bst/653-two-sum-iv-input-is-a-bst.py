# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dictt = {}
        def helper(root):
            nonlocal dictt
            if root == None: return False
            val = root.val
            if val in dictt.keys(): 
                return True
            dictt[k - val] = val 
            if helper(root.left) or helper(root.right):
                return True
            return False
        return helper(root)
            