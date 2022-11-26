class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k: return False
        c = Counter(nums)
        Heap = list(c.keys())
        heapify(Heap)
        queue = deque([])
        
        while Heap:
            start = Heap[0]
            for i in range(k):
                if not Heap: return False
                num = heappop(Heap)
                if num != start + i: return False
                c[num] -= 1
                if c[num] > 0: queue.append(num)
            while queue:
                heappush(Heap, queue.popleft())
        return True