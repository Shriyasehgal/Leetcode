class Solution:
    def buildGraph(self, points):
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                graph[i].append((dist,j))
                graph[j].append((dist,i))
        return graph
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = self.buildGraph(points)

        heap = [(0,0)] #(distance, destination)
        visited = [0]*len(points)
        totalCost = 0
        while heap:
            point = heappop(heap)
            if visited[point[1]] == 1: continue
            totalCost += point[0]
            visited[point[1]] = 1
            for n in graph[point[1]]:
                if visited[n[1]] != 1:
                    heappush(heap,n)
                   
        return totalCost
        
        