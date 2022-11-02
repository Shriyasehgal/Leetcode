class Solution:
    def buildGraph(self, equations, values):
        graph = defaultdict(list)
        for i,(x,y) in enumerate(equations):
            graph[x].append((y,values[i]))
            graph[y].append((x,1/values[i]))
        return graph 
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations,values)
        res = []
        def bfs(query):
            start,end = query
            if start not in graph: return -1
            q1 = deque([(start,1)])
            q2 = deque()
            visited = set([start])
            
            while q1:
                elem , val = q1.popleft()
                if elem == end:
                    graph[start].append((end,val))
                    graph[end].append((start,1/val))
                    return val
                for neigh in graph[elem]:
                    (n,nextVal) = neigh
                    if n not in visited:
                        q2.append((n,val*nextVal))
                        visited.add(n)
                if not q1:
                    q1,q2 = q2,q1
            return -1
        for query in queries:
            res.append(bfs(query))
        return res