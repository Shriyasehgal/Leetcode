'''Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)'''



#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
         
class LinkedList(object):
    def __init__(self):
        self.head=None
        
    def printList(self):
        temp=self.head
        list=[]
        while(temp):
            list.append(temp.val)
            temp=temp.next
        print(list)
            
    def appendatend(self,new_data):
        newNode=ListNode(new_data)
        if self.head is None:
            self.head=newNode
            return
        last=self.head
        
        while(last.next):
            last=last.next
       
        last.next=newNode
        return
    
    
    def appendatstart(self,new_data):
        newNode=ListNode(new_data)
        if self.head is None:
            self.head=newNode
            return
        newNode.next=self.head
        self.head=newNode
        return
    
    
class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        
        prev = None 
        curr1 = head
        curr2 = head.next
        
        while True:
            after = curr2.next
            curr1.next = after
            curr2.next = curr1
            
            if prev == None:
                prev = curr2
                start = prev
            else:
                prev.next = curr2
            
            if curr1.next != None and curr1.next.next!=None:
                prev = curr1
                curr1 = curr1.next
                curr2 = curr1.next
               
            else:
                break
                
        return start
    
            
            
            
L1 = input()

list1=LinkedList()

for i in range(0,len(L1)):
    list1.appendatend(L1[i])
    
sol= Solution()
swap= sol.swapPairs(list1.head)
