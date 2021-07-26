'''Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        # find middle
        mid = (len(nums)) / 2

        # make the middle element the root
        root = TreeNode(nums[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
