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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        
        curr=head
        
        while curr!=None and curr.next!=None:
            s=curr
            e=curr.next
            
            currDummy=head
            s_prev=None
            while currDummy!=s:
                s_prev=currDummy
                currDummy=currDummy.next
                
            e_prev=s
                
                
            if s_prev!=None:
                s_prev.next=e
            else:
                head=e
                    
            e_prev.next=s
                
            temp=s.next
            s.next=e.next
            e.next=temp  
            
            curr=curr.next
        return head
    
            
            
            
L1 = input()

list1=LinkedList()

for i in range(0,len(L1)):
    list1.appendatend(L1[i])
    
sol= Solution()
swap= sol.swapPairs(list1.head)
