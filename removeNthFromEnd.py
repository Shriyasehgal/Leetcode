#Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i=head
        j=head
        count=1
        
        
        while count<=n:
            i=i.next
            count+=1
            
        if i==None:
            return head.next
            
        while i.next!= None:
            i=i.next
            j=j.next
            
        j.next=j.next.next
        
        return head
