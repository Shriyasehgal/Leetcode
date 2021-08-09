'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum ):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root==None:
            return False


        #Checking if the node is a leaf
        def isLeaf(node):
            if node.right==None and node.left==None:
                return True
            return False

        def helper(root, rem_sem) :
            if rem_sem==0 and isLeaf(root):     #The Path exists
                return True

            if root.left:                       #Check only if the left node exists
                print(rem_sem-root.left.val)
                if helper(root.left,rem_sem-root.left.val):
                    return True

            if root.right:                       #Check only if the right node exists
                if helper(root.right,rem_sem-root.right.val):
                    return True

            return False

        return helper(root,targetSum-root.val)
