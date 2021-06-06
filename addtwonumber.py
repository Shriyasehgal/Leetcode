# Definition for singly-linked list.
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
"""
         
        temp=l1.val
        while(l1.next):
            temp=temp*10 + l1.next.val     
            l1=l1.next
        
        rev=0
        while temp!=0:
            pop=temp%10
            temp=temp/10
            temp1=rev*10+pop
            rev=temp1
        
        
        
        temp=l2.val
        while(l2.next):
            temp=temp*10 +l2.next.val            
            l2=l2.next
        
        
        rev1=0
        while temp!=0:
            pop1=temp%10
            temp=temp/10
            temp1=rev1*10+pop1
            rev1=temp1
     
        
        add=rev+rev1
        add=list(map(int,str(add)))
        
        sollist=LinkedList()
        for i in range(0,len(add)):
            sollist.appendatstart(add[i])
            
        return sollist
        
        
        
L1 = input()
L2 = input()



list1=LinkedList()
list2=LinkedList()

for i in range(0,len(L1)):
    list1.appendatend(L1[i])

for i in range(0,len(L2)):
    list2.appendatend(L2[i])
    
sol= Solution()
add= sol.addTwoNumbers(list1.head,list2.head)
#sollist=LinkedList()
#for i in range(0,len(add)):
 #   sollist.appendatstart(add[i])


    

