class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        words = [(-v,k) for k,v in c.items()]
        heapify(words)
        res = []
        while k :
            res.append(heappop(words)[1])
            k-=1
        return res
        