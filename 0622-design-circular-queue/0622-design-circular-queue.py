class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int): 
        self.f = None
        self.r = None
        self.k = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.k: return False
        if self.f == None:
            self.f = Node(value)
            self.r = self.f
        else:
            self.r.next = Node(value)
            self.r = self.r.next
        self.count += 1
        return True
            

    def deQueue(self) -> bool:
        if self.count == 0: return False
        prev = self.f
        self.f = self.f.next
        del prev
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.count == 0: 
            return -1
        
        return self.f.val
        

    def Rear(self) -> int:
        if self.count == 0: return -1
        return self.r.val

    def isEmpty(self) -> bool:
        if self.count == 0: return True
        

    def isFull(self) -> bool:
        if self.count == self.k: return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()