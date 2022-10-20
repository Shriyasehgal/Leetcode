#User function Template for python3
from collections import defaultdict

class Solution:
    
    def buildGraph(self,edges):
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
        return graph
            
        
    def possible_paths(self, edges, n, s, d):
        ways = 0
        graph = self.buildGraph(edges)
        visited = set()
        def dfs(curr):
            nonlocal ways
            if curr == d:
                ways+=1
                return
            if curr in visited: return
            visited.add(curr)
            for i in graph[curr]:
                dfs(i)
            visited.remove(curr)
        dfs(s)
        return ways
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, s, d = input().split()
		n = int(n); m = int(m); s = int(s); d = int(d);
		edges = []
		for _ in range(m):
		    x,y = input().split()
		    x = int(x); y = int(y);
		    edges.append([x,y])
		obj = Solution()
		ans = obj.possible_paths(edges, n, s, d)
		print(ans)


# } Driver Code Ends