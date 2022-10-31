# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode], dp ={}) -> int:
        if not root: return 0
        if root in dp: return dp[root]
        #Choosing to select the root node
        #We can only select its gradchildren now
        ll,lr,rl,rr = 0,0,0,0
        if root.left:
            ll = self.rob(root.left.left,dp)
            lr = self.rob(root.left.right,dp)
        if root.right:
            rl = self.rob(root.right.left,dp)
            rr = self.rob(root.right.right,dp)
        selectRoot = root.val + ll + lr + rl + rr
        
        #Choosing to not select the root node
        l = self.rob(root.left,dp)
        r = self.rob(root.right,dp)
        notSelectRoot = l+r
        
        dp[root] = max(selectRoot, notSelectRoot)
        return dp[root]
    