'''Return min using stack'''


class Stack(object):
    def __init__(self):
        self.stack=[]
        self.aux=[]
        
    def push(self, element):
        if len(self.aux)==0:
            self.aux.append(element)
        else:
           self.aux.append(min(element, self.aux[-1]))
                   
        self.stack.append(element)
        
    def pop(self):
        self.aux.pop()
        return self.stack.pop()
        
    def getmin(self):
        return self.aux[-1]
        
    def isempty():
        if len(self.stack)==0:
            return True
        else:
            return False
            
            
stack=Stack()
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(1)
stack.push(5)
stack.getmin()
stack.pop()
stack .getmin()
        
        
