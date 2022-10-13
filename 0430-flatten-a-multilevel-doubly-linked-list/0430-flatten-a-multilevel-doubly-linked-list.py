"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dummy = Node(0,None,None,None)
        curr = dummy
        def dfs(head):
            nonlocal curr
            if head == None: 
                return 
            
            curr.next = Node(head.val,None, None, None)
            
            currPrev = curr
            curr = curr.next
            curr.prev = currPrev
            dfs(head.child)
            dfs(head.next)
            
        dfs(head)
        dummy = dummy.next
        dummy.prev = None
        return dummy
    
        