class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {k : [] for k in range(len(points))}
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adjList[i].append((dist,j)) # cost, neigh
                adjList[j].append((dist,i))
       #Prim's algothim
        visited = set()
        minH = [[0,0]]
        res = 0
        while len(visited) < len(points):
            cost,n = heapq.heappop(minH)
            if n in visited:
                continue
            res+=cost
            visited.add(n)
            for neighbor in adjList[n] :
                if neighbor not in visited:
                    heapq.heappush(minH,neighbor)
        return res
                