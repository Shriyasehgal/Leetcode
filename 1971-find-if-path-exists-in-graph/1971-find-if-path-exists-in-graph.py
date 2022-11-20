class Solution:
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return graph
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.buildGraph(edges)
        q1 = deque([source])
        q2 = deque()
        visited = set([source])
        while q1:
            node = q1.popleft()
            if node == destination: return True
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    q2.append(i)
            if not q1:
                q1,q2 = q2,q1
        return False