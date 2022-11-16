class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(x):
            p = parent[x]
            if x == p:
                return p
            else: return find(p)
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return True
            else:
                parent[p2] = p1
            return False
            
        for x,y in edges:
            if union(x,y): return [x,y]
            
        ''' graph = defaultdict(list)
        for a,b in edges:
            if not self.dfs(a,b,graph, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
            
        
    def dfs(self, start, target, graph,visited):
        if start in visited:
            return True
        if start == target:
            return False
        visited.add(start)
        for n in graph[start]:
            if not self.dfs(n,target,graph,visited): return False
        return True'''