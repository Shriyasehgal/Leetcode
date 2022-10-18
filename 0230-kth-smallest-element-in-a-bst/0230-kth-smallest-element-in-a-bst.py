# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pre = []
        def dfs(root):
            if root == None: return
            dfs(root.left)
            pre.append(root.val)
            dfs(root.right)
        dfs(root)
        return pre[k-1]
                