class Solution:
    def buildGraph(self, times):
        timeGraph = defaultdict(list)
        for i in range(len(times)):
            s,d,c = times[i]
            timeGraph[s].append([d,c])
        return timeGraph
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times = self.buildGraph(times)
        heap = [(0,k)]
        heapify(heap)
        allCost = []
        visited = set()
        while heap:
            cost,s = heappop(heap)
            if s in visited: continue
            visited.add(s)
            allCost.append(cost)
            for d,c in times[s]:
                heappush(heap,(c+cost,d))
        if len(visited) < n: return -1
        return max(allCost)
            
        