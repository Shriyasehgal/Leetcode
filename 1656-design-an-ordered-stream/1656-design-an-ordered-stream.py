class OrderedStream:

    def __init__(self, n: int):
        self.chunkList = ['']*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunkList[idKey-1] = value
        res = []
        while self.ptr < len(self.chunkList) and self.chunkList[self.ptr]!='':
            res.append(self.chunkList[self.ptr])
            self.ptr+=1
        
        return res
    

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)