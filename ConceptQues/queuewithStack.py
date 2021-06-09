#Implementation of Queue with Stack


class queuewithStack(object):
    
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def enqueue(self, element):
        while(len(self.s1))!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        self.s1.append(element)
        
        while(len(self.s2))!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
            
        
        
    def dequeue(self):
        if len(self.s1)==0:
            print("Queue is Empty")
        else:
            self.s1.pop()
 
 
 
queue=queuewithStack()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.enqueue(5)
queue.dequeue()
