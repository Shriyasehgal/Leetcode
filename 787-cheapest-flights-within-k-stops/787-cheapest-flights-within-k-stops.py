class Solution:
            
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices =[[float('inf') for i in range(n)] for i in range(k+2)]
        prices[0][src] = 0
        for i in range(1,len(prices)):
            prices[i] = prices[i-1].copy()
            for s,d,p in flights:
                if prices[i-1][s] == float('inf'): continue
                if prices[i-1][s] + p < prices[i][d]:
                    prices[i][d] = prices[i-1][s] + p
        return prices[-1][dst] if prices[-1][dst]!=float('inf') else -1
                