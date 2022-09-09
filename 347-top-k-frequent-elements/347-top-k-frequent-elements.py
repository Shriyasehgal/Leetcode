from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = [(-i,j) for (j,i) in c.items()]
        heapify(heap)
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
            
        