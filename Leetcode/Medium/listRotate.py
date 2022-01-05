'''Given the head of a linked list, rotate the list to the right by k places.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 1
        #Base case
        if curr == None or curr.next == None:
            return head
        #Reaching the end of the list
        while curr.next!=None:
            curr = curr.next 
            count+=1
 
        
        #creating a cycle
        curr.next = head
        
        
        m = count- k%count
      
        #Reaching the new beginning of the list
        while m!=0:
            curr = curr.next
            m-=1
     
        #Changing the head and the tail
        head = curr.next
        curr.next = None
        
        return head
        
        
      
          
       
            
