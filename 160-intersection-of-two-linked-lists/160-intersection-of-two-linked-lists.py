# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        #Changing th position of the head so that the length of both the lists become equal
        while curA or curB:
            if curA:
                curA = curA.next
            else:
                headB = headB.next
            if curB:
                curB = curB.next
            else:
                headA = headA.next
        while headA and headA!=headB:
            
            headA = headA.next
            headB = headB.next
        return headA
            