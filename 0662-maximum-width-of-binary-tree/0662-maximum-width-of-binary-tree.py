# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q1 = deque([(root,0)])
        q2 = deque()
        maxWidth = 1
        while q1:
            node = q1.popleft()
            order = node[1]
            q2.append((node[0].left,2*order+1)) if node[0].left else None
            q2.append((node[0].right, 2*order+2)) if node[0].right else None
            if not q1:
                if q2:
                    maxWidth = max(maxWidth, q2[-1][1]-q2[0][1]+1)
                q1,q2 = q2,q1
        return maxWidth