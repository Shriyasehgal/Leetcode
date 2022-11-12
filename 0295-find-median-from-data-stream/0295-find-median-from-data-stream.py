class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []


    def addNum(self, num: int) -> None:
        # first offer to max heap
        heappush(self.maxHeap, -num)
        # bring highest of maxheap to min heap
        heappush(self.minHeap, -heappop(self.maxHeap))
        
        # if heaps become unbalanced
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        # if stream is odd
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        # else mean of mids
        return (-self.maxHeap[0] + self.minHeap[0]) * 0.5

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()