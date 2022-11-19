# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr = head
        count = 1
        while curr.next:
            count+=1
            curr = curr.next
        curr.next = head
        k = count - k%count
        while k != 0:
            curr = curr.next
            k-=1
        newHead = curr.next
        curr.next = None
        return newHead
        