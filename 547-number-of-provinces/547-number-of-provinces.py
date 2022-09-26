class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
                return parent[x]
            if parent[x] == x:
                return parent[x]
            return find(parent[x])
        
        def union(X,Y):
            x = find(X)
            y = find(Y)
            #They are already connected we dont need to connect them ahead.
            if x == y:
                return False
            parent[y] = x
            return True
        
        res = len(isConnected)
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j] == 1 and union(i,j):
                    res-=1
        return res
                    
        
        
            
        