# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i in range(len(inorder) ):
            inorder_dict[inorder[i]] = i
        return self.helper(preorder, inorder, inorder_dict)
            
    def helper(self,preorder,inorder, inorder_dict):    
        root = TreeNode(preorder[0])
        i = inorder_dict[preorder[0]]
        root.left = self.buildTree(preorder[1:i+1], inorder[0:i]) if len(preorder[1:i+1]) > 0 else None
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:]) if len(preorder[i+1:]) > 0 else None
        return root