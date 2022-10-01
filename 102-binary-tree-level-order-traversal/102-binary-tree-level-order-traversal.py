# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        final_res = []
        oldQueue = deque([root]) if root else None
        newQueue = deque([])
        while oldQueue:
            res = []
            for i in range(len(oldQueue)):
                elem = oldQueue.popleft()
                res.append(elem.val)
                newQueue.append(elem.left) if elem.left else None
                newQueue.append(elem.right) if elem.right else None
                
            final_res.append(res)
            oldQueue,newQueue = newQueue,oldQueue
        return final_res
        