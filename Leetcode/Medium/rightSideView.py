# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue1 = [root]
        queue2 = []
        output = []
        
        while queue1:
            output.append(queue1[-1].val) 
            for i in range(len(queue1)):
                queue2.append(queue1[i].left) if queue1[i].left else None
                queue2.append(queue1[i].right) if queue1[i].right else None
            queue1 = queue2
            queue2 = []
            
        return output
                
                
