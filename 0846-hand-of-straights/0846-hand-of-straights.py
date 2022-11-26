class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        c = Counter(hand)
        cardHeap = list(c.keys())
        heapify(cardHeap)
        queue = deque([])
        
        while cardHeap:
            start = cardHeap[0]
            k = 0
            for _ in range(groupSize):
                if not cardHeap: return False
                card = heappop(cardHeap)
                if card != start + k: return False
                c[card] -= 1
                if c[card] > 0: queue.append(card)
                k+=1
            while queue:
                heappush(cardHeap, queue.popleft())
        return True
                
                
                