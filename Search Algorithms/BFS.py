from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bst(self,s):
        queue=[]
        visited = [False] * (max(self.graph) + 1)

        queue.append(s)
        visited[s]=True

        while queue:
            s=queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i]=True
                    queue.append(i)


    


graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.addEdge(5,1)
graph.addEdge(1,3)
graph.bst(2)
