# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #find the mid point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        
        i = self.sortList(head)
        j = self.sortList(head2)
        
        dummy = ListNode(0)
        temp = dummy
        while i and j:

            if i.val <= j.val:
                dummy.next = i
                i = i.next
            else:
                dummy.next = j
                j = j.next
            dummy = dummy.next
        if i:
            dummy.next = i

        if j:
            dummy.next = j


        return temp.next
