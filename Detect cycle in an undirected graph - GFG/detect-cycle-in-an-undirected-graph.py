

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
        def dfs(s, prev):
            if s in visited: return True
            visited.add(s)
            for d in adj[s]:
                if d == prev: continue
                if dfs(d,s): return True
            visited.remove(s)
            return False
        for i in range(V):
            if dfs(i, None): return True
        return False
            
            

#{ 
 # Driver Code Starts


if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends