from collections import defaultdict
from heapq import heappush, heappop
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        
        res = [-1 for i in range(V)]
        heap = [(0,S)]
        visited = set()
        while heap:
            wi,di = heappop(heap)
            if di in visited: continue
            visited.add(di)
            res[di] = wi
            for dj,wj in adj[di]:
                heappush(heap, (wi+wj,dj))
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends