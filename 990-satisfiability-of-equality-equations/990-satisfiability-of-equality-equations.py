class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent.keys():
                parent[x] = x
                return parent[x]
            if parent[x] == x:
                return parent[x]
            return find(parent[x])
            
        def union(X,Y):
            x = find(X)
            y = find(Y)
            #Incase both of them have a same parent, they are already connected.
            if x == y:
                return
            #Incase they have a different paren
            parent[y] = x
        
        for i in range(len(equations)):
            if equations[i][1] == '=':
                union(equations[i][0],equations[i][3])
                    
        for i in range(len(equations)):
            if equations[i][1] == '!':
                if find(equations[i][0]) == find(equations[i][3]):
                    return False
        return True
        