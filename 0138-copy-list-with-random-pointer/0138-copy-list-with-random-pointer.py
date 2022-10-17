"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        NodeMap = {}
        curr = head
        while curr:
            newNode = Node(curr.val)
            NodeMap[curr] = newNode
            curr = curr.next
        curr = head
        while curr:
            NodeMap[curr].next = NodeMap[curr.next] if curr.next else None
            NodeMap[curr].random = NodeMap[curr.random] if curr.random else None
            curr = curr.next
        return NodeMap[head]