class RandomizedSet:

    def __init__(self):
        self.set = []
        self.map = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.set.append(val)
        self.map[val] = self.count
        self.count+=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        self.map[self.set[-1]] = idx
        self.set[idx], self.set[-1] = self.set[-1], self.set[idx]
        self.set.pop()
        self.count -=1
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        i = random.randint(0,self.count-1)
        return self.set[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()