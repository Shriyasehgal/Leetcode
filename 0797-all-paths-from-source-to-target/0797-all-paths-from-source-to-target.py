class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(i, curr):
            if i in visited: return
            if i == len(graph) - 1:
                res.append(curr[:])
                return
            visited.add(i)
            for j in graph[i]:
                dfs(j, curr + [j])
            visited.remove(i)
        dfs(0,[0])
        return res