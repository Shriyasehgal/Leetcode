class Solution:
    def buildGraph(self,numCourses, prerequisites):
        graph = {k:[] for k in range(numCourses)}
        for pre in prerequisites:
            c1,c2 = pre
            graph[c1].append(c2)
        return graph
        
    def hasCycle(self, node, visited, graph):
        if visited[node] == 1:
            return True
        if graph == []:
            return False
        visited[node] = 1
        for n in graph[node]:
            if self.hasCycle(n, visited,graph):
                return True
        visited[node] = 0
        graph[node] = [] #Because we know we can complete this course given all its prerequisites, we can change it back to an empty list so that we dont have to perform recurssion for every value.
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses,prerequisites)
        visited = [0]*(numCourses)
        for node in graph.keys():
            if self.hasCycle(node, visited, graph):
                return False
        return True