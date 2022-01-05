'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        cur1 = head
        cur2 = head.next
        prev = ListNode(0,cur1)
        prev2 = prev
        
        while cur2 != None:
            while cur2!=None and cur1.val == cur2.val:
                cur2 = cur2.next
                
            if cur2 == cur1.next:
                prev = cur1
                
            else:
                prev.next = cur2
            
            cur1 = cur2
            cur2 = cur2.next if cur2 else None
        return prev2.next
