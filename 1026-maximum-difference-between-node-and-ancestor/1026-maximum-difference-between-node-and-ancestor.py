# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0
        def dfs(root, maxx, minn):
            nonlocal maxDiff
            if root == None:
                return
            maxDiff = max(maxDiff, abs(maxx - root.val), abs(minn-root.val))
            if maxx < root.val:
                maxx = root.val
            if minn > root.val:
                minn = root.val
            dfs(root.left, maxx, minn)
            dfs(root.right, maxx, minn)
        dfs(root, root.val, root.val)
        return maxDiff