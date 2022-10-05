# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        k = 1
        if depth == 1:
            newNode = TreeNode(val=val,left = root)
            oldQueue = deque([newNode])
            return newNode
        else:
            oldQueue = deque([root])
        newQueue = deque([])
        while k < depth-1 and oldQueue:
            elem = oldQueue.popleft()
            newQueue.append(elem.left) if elem.left else None
            newQueue.append(elem.right) if elem.right else None
            if not oldQueue:
                k+=1
                newQueue, oldQueue = oldQueue, newQueue
        while oldQueue:
            elem = oldQueue.popleft()
            left_temp = elem.left if elem.left else None
            right_temp = elem.right if elem.right else None
            elem.left = TreeNode(val = val, left = left_temp, right = None)
            elem.right = TreeNode(val = val, left = None, right = right_temp)
        return root
                
        
            