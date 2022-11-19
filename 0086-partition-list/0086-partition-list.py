# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        temp1, temp2 = dummy1, dummy2
        curr = head
        while curr:
            
            if curr.val < x:
                dummy1.next = curr
                dummy1 = dummy1.next
            else:
                dummy2.next = curr
                dummy2 = dummy2.next
            curr = curr.next
            
        dummy1.next = temp2.next        
        dummy2.next = None
        return temp1.next
        