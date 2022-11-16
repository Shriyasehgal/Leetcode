class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        provinces = len(isConnected)
        def find(x):
            p = parent[x]
            if x == p: return x
            else: return find(p)
        def union(x,y):
            nonlocal provinces
            p1 = find(x)
            p2 = find(y)
            if p1 == p2: 
                return
            else:
                provinces -= 1
                parent[p2] = p1
        for i in range(0,len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i,j)
        return provinces
                    
                