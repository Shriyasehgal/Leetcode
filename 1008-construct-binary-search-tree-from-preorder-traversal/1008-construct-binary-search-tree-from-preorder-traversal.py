# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        def helper(lower, upper):
            if preorder and preorder[0] > lower and preorder[0] < upper:
                val = preorder.popleft()
                newNode = TreeNode(val)
                newNode.left = helper(lower,val)
                newNode.right = helper(val, upper)
                return newNode
            else:
                return None
        
        return helper(-float('inf'), float('inf'))