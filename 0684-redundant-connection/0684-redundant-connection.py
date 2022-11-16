class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
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
        return True