'''You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head.next==None:
            return head
        i=1
        s=head
        temp=head
        e=head
        #Kth Node from the begining 
        while i<k:   
            s=s.next
            temp=temp.next
            i+=1
        
        #kth node from the end
        while temp.next!=None:
            temp=temp.next
            e=e.next
        
        if e==s:                #when swapping nodes are the same
            return head
        
        s_prev=None             #Getting previous node of S
        curr=head
        while curr!=s:
            s_prev=curr
            curr=curr.next
        
        e_prev=None             #Getting te previous node of e
        curr=head
        while curr!=e:
            e_prev=curr
            curr=curr.next
        
        
        if s_prev !=None:          #if s is not head
            s_prev.next=e
        else:
            head=e
            
        if e_prev!=None:          #if s is not head
            e_prev.next=s
        else:
            head=s
        
            
        temp = s.next             #swapping
        s.next = e.next
        e.next = temp
        
        return head
        
