# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        dummy = ListNode(0,head)
        while curr: 
            n+=1
            curr = curr.next
        curr = dummy
        n = n//2
        while n: 
            curr = curr.next
            n-=1
        curr.next = curr.next.next
        return dummy.next
            