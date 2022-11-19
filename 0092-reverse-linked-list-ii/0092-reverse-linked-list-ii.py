# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head: return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for i in range(1,left):
            curr = curr.next
            prev = prev.next
        leftTemp = prev
        rightTemp = curr
        for i in range(left,right+1):
            nexx = curr.next
            curr.next = prev
            prev = curr 
            curr = nexx
        leftTemp.next = prev
        rightTemp.next = curr
        return dummy.next
        
            