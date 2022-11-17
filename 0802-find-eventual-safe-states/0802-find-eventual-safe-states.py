class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        res = []
        added = set()
        def dfs(i):
            if i in visited:
                return False
            if i in added:
                return True
            
            visited.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            graph[i] = []
            res.append(i)
            visited.remove(i)
            added.add(i)
            return True
        for i in range(len(graph)):
            dfs(i)
        res.sort()
        return res
            
        