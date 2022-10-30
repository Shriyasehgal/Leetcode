class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            grid[i][j] = 1
            if i > 0 and grid[i-1][j] == 0:
                dfs(i-1,j,visited)
            if i < len(grid)-1 and grid[i+1][j] == 0:
                dfs(i+1, j, visited)
            if j > 0 and grid[i][j-1] == 0:
                dfs(i,j-1,visited)
            if j < len(grid[0])-1  and grid[i][j+1] == 0:
                dfs(i,j+1,visited)
        res = 0     
        #first and last row
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                dfs(0,j,set())
            if grid[len(grid)-1][j] == 0:
                dfs(len(grid)-1,j,set())
        #first and last col
        for i in range(len(grid)):
            if grid[i][0] == 0:
                dfs(i,0,set())
            if grid[i][len(grid[0])-1] == 0:
                dfs(i,len(grid[0])-1,set())
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res+=1
                    dfs(i,j,set())
        return res
            
                
            
            