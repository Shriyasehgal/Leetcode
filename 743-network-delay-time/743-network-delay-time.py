class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for i,j,w in times:
            adjList[i].append([w, j])
        visited = set()
        allCost = []
        minH = [[0,k]]
        while minH:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            allCost.append(cost)
            visited.add(node)
            for neigh in adjList[node]:
                if neigh[1] not in visited:
                    neigh[0]+=cost
                    heapq.heappush(minH,neigh)
        if len(visited) < n: return -1
        return max(allCost)