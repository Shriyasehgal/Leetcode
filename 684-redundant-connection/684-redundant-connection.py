class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = []
        visited = [0]*(len(edges))
        for u,v in edges:
            if self.dfs(u,v,graph,visited[:]):
                ans = u,v
            graph[u].append(v)
            graph[v].append(u)
        return ans
    #The idea is before adding an edge, check if we can reach from e1 to e2 through the existing edges in the   graph.
    def dfs(self,u,v,graph,visited):
        if visited[u-1] == 1:
            return False
        #We found another path from u to v, hence adding a new node (u,v) is going to cause a cycle.
        if u == v:
            return True
        visited[u-1] = 1
        for n in graph[u]:
            if self.dfs(n,v,graph,visited):
                return True
        return False
        
        