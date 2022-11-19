# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: return None
        #Searching the element if it is not equal to the root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        #Once we have found the key in the root
        else:
            # We have 4 posibilities
            #This is the leaf node
            if not root.left and not root.right: return None
            #2 If there is no root.left
            elif not root.left:
                return root.right
            #3 There is no root.right
            elif not root.right:
                return root.left
            else:
                temp = root
                temp = temp.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
                    
            