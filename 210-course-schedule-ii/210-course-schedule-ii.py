class Solution:
    def buildGraph(self, numCourses, prerequisites):
        courseGraph = {k:[] for k in range(numCourses) }
        for pre in prerequisites:
            c1,c2 = pre
            courseGraph[c1].append(c2)
        return courseGraph
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites) # to build an ajc list
        visited = [0]*numCourses # This is to check for any cycle
        checked = [0]*numCourses # This is for dfs to add the courses in the output.
        output = [] # This is to add the course in the order
        def buildOrder(node):
            #There is a cycle
            if visited[node] == 1:
                return False 
            #We have added the course in the output. So we dont add the courses twice.
            if checked[node] == 1:
                return True
            visited[node] = 1
            #For all the prereq of the courses.
            for n in graph[node]:
                if not buildOrder(n):
                    return False
            #We are no longer checking this path, so change it back to 0
            visited[node] = 0
            #All the prereq have been added to the list, so now we can add this course.
            checked[node] = 1
            output.append(node)
            return True
        
        for c in range(numCourses):
            if buildOrder(c) == False:
                return []
        return output
        
            