class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [[float('inf') for i in range(n) ] for j in range(k+2)]
        price[0][src] = 0
        for i in range(1,len(price)):
            price[i] = price[i-1][:]
            for s,d,p in flights:
                if price[i-1][s] == float('inf'): continue
                if price[i-1][s] + p < price[i][d]:
                    price[i][d] = price[i-1][s] + p
        print(price)
        return price[-1][dst] if price[-1][dst]!=float('inf') else -1
                