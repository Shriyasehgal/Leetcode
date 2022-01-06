'''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right or head.next == None:
            return head
        
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        for i in range(1, left):
            curr = curr.next
            prev = prev.next
        l = curr
        temp = prev
        for i in range(left, right+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        temp.next = prev
        l.next = curr
        
        return dummy.next
        
            
