from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self,s):


        stack=[]
        visited = [False] * (max(self.graph) + 1)

        stack.append(s)
        visited[s]=True

        while stack:
            s=stack.pop()
            print(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i]=True
                    stack.append(i)





graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.addEdge(5,1)
graph.addEdge(1,3)
graph.dfs(1)
