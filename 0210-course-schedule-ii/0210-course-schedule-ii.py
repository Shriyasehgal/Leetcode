class Solution:
    def buildGraph(self, pre):
        graph = defaultdict(list)
        for a,b in pre:
            graph[a].append(b)
        return graph
            
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(prerequisites)
        visited = [0]*numCourses
        taken = [0]*numCourses
        res = []
        def canTake(i):
            if taken[i] == 1:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for n in graph[i]:
                if not canTake(n):
                    return False
            visited[i] = 0
            graph[i] = []
            taken[i] = 1
            res.append(i)
            return True
        for i in range(numCourses):
            if not canTake(i): return []
        return res
                
            