from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        queue = [root]
        newQueue = []
        while queue:
            if level%2 == 1:
                l = 0
                r = len(queue) - 1
                while l <= r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l+=1
                    r-=1
                    
            for i in range(len(queue)):
                curr = queue.pop(0)
                newQueue.append(curr.left) if curr.left else None
                newQueue.append(curr.right) if curr.right else None
        
            level +=1
            queue = newQueue[:]
            newQueue.clear()
        return root
        