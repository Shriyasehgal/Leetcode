'''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths=[]

        def helper(root,rem_sum,path):

            if rem_sum==0 and root.right==None and root.left== None:

                paths.append(path[:])
                return


            if root.left:
                path.append(root.left.val)
                helper(root.left,rem_sum-root.left.val,path)
                path.pop()

            if root.right:
                path.append(root.right.val)
                helper(root.right,rem_sum-root.right.val,path)
                path.pop()

        if not root:
            return []
        helper(root,targetSum-root.val,[root.val])
        return paths
