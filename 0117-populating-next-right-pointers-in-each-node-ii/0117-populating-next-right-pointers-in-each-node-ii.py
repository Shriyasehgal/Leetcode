"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None : return None
        oldQueue = deque([root])
        newQueue = deque([])
        prev = None
        while oldQueue:
            curr = oldQueue.popleft()
            newQueue.append(curr.left) if curr.left else None
            newQueue.append(curr.right) if curr.right else None
            if prev:
                prev.next = curr
            prev = curr
            if not oldQueue:
                curr.next = None
                prev = None
                newQueue, oldQueue = oldQueue,newQueue
        return root
                
                
            
            