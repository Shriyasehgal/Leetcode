class MyQueue(object):

    def __init__(self):
        self.stack1 = [] #The represents the back of the queue
        self.stack2 = [] #This represents the front of the queue

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.frontToBack()
        return self.stack2.pop()
       
        

    def peek(self):
        """
        :rtype: int
        """
        self.frontToBack()
        val = self.stack2.pop()
        self.stack2.append(val)
        return val
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
    
    def frontToBack(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()