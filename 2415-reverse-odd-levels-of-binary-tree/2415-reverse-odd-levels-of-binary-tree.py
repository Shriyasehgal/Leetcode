from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Traverse Once
        flag = 0
        queue = [root]
        newQueue = []
        auxQueue = []
        aux = []
        while queue:
            el = queue.pop(0)
            newQueue.append(el.left) if el.left else None
            newQueue.append(el.right) if el.right else None
            aux.append(el.val)
            if not queue:
                if flag == 0:
                    
                    aux.clear()
                    flag = 1
                elif flag == 1:
                    auxQueue.append(aux[:])
                    aux.clear()
                    flag = 0
                queue = newQueue[:]
                newQueue = []
        queue = [root]
        newQueue = []
        flag = 0
        while queue:
            if flag == 0:
                el = queue.pop(0)
                newQueue.append(el.left) if el.left else None
                newQueue.append(el.right) if el.right else None
                if not queue:
                    queue = newQueue[:]
                    newQueue = []
                    flag = 1
                    aux = auxQueue.pop(0) if auxQueue else None
            
            elif flag == 1:
                el = queue.pop(0)
                el.val = aux.pop()
                newQueue.append(el.left) if el.left else None
                newQueue.append(el.right) if el.right else None
                if not queue:
                    queue = newQueue[:]
                    newQueue = []
                    flag = 0
            
                
            
        return root
            
        
                
        