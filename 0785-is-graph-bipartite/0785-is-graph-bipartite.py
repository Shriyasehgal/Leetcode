class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #this is the graph coloring algorithm
        
        color = [None]*len(graph)
        
        
        for i in range(len(graph)):
            if color[i] == None:
                color[i] = 1
            q1 = deque([i])
            q2 = deque()
            visited = set()
            while q1:
                node = q1.popleft()
                for n in graph[node]:
                    if color[n] == None:
                        color[n] = 1-color[node]
                        if n not in visited: q2.append(n)
                    elif color[n] == color[node]:
                        return False
                visited.add(node)
                if not q1:
                    q1,q2 = q2,q1

        
        return True