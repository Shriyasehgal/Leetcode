class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'),-1)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx +=1
        while self.stack[-1][0] <= price:
                self.stack.pop()
        val = self.idx - self.stack[-1][1]
        self.stack.append((price,self.idx))
        return val
        
                
                


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)