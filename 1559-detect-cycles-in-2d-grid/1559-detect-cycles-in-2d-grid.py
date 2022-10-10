class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def dfs(curr,prev,visited,value):
            i1 = curr[0] #current elements
            j1 = curr[1] #current elements
            i0 = prev[0] #previous elements
            j0 = prev[1] #previous elements
            if curr in visited:
                return True
            if grid[i1][j1] != value: return False
            visited.add(curr)
            if i1 > 0 and i1-1!=i0:
                if dfs((i1-1,j1),(i1,j1),visited,value): return True
                
            if j1 > 0  and j1-1!=j0:
                if dfs((i1,j1-1),(i1,j1),visited,value): return True
                
            if i1 < len(grid)-1  and i1+1!=i0:
                if dfs((i1+1,j1),(i1,j1),visited,value): return True
            
            if j1 < len(grid[0])-1 and j1+1!=j0:
                if dfs((i1,j1+1),(i1,j1),visited,value): return True
            grid[i1][j1] = '*'
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!='*' and dfs((i,j),(None,None),set(),grid[i][j]):
                    return True
        return False
                
        