class RandomizedSet(object):

    def __init__(self):
        self.randomSet = {}
        self.elements = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomSet: 
            return False
        else: 
            self.elements.append(val)
            self.randomSet[val] = len(self.elements)-1
        return True
            
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.randomSet: return False
        idx = self.randomSet[val]
        self.randomSet[self.elements[-1]] = idx
        self.elements[idx], self.elements[-1] = self.elements[-1], self.elements[idx]
        self.elements.pop()
        del self.randomSet[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        
        return self.elements[random.randint(0, len(self.elements) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()