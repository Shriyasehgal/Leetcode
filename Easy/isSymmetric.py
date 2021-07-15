'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).'''







# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        curr_right=root
        curr_left=root

        def helper(root_1,root_2):
            if root_1==None and root_2==None:
                return True
            elif (root_1==None) != (root_2==None):
                return False

            if root_1.val==root_2.val:
                condition= helper(root_1.left,root_2.right)
                if condition == True:
                    cond2 = helper(root_1.right,root_2.left)
                    return cond2
            return False

        return helper(curr_left,curr_right)
