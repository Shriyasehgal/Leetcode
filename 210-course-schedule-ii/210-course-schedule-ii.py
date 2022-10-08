class Solution:
    def buildGraph(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        return graph
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        visited = set() #to check the current cycle
        taken = set() # to check which courses we have already taken
        res = []
        def helper(i):
            if i in taken: return True
            if i in visited : return False
            visited.add(i)
            for n in graph[i]:
                if not helper(n):
                    return False
            taken.add(i)
            res.append(i)
            graph[i] = []
            visited.remove(i)
            return True
        for i in range(numCourses):
            if not helper(i): return []
        return res
                