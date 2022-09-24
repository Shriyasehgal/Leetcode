# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        res = []
        def helper(root, curr, val):
            if root.right == None and root.left == None:
                if val == targetSum:
                    res.append(curr)
                    return
                else:
                    return
            helper(root.left, curr+[root.left.val], val+root.left.val) if root.left else None
            helper(root.right, curr+[root.right.val], val+root.right.val) if root.right else None
        helper(root,[root.val],root.val)
        return res