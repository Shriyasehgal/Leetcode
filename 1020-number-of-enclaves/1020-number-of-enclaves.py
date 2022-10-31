class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j,visited):
            if (i,j) in visited: return 
            visited.add((i,j))
            num = 1
            grid[i][j] = 0
            if i > 0 and grid[i-1][j] == 1:
                num+=dfs(i-1,j,visited)
            if i < len(grid)-1 and grid[i+1][j] == 1:
                num+=dfs(i+1,j,visited)
            if j > 0 and grid[i][j-1] == 1:
                num+=dfs(i,j-1,visited)
            if j < len(grid[0])-1 and grid[i][j+1] == 1:
                num+=dfs(i,j+1,visited)
            return num
                
        #Checking the borders
        for j in range(len(grid[0])):
            if grid[0][j] == 1:
                _ = dfs(0,j,set())
            if grid[len(grid)-1][j] == 1:
                _ = dfs(len(grid)-1,j,set())
        for i in range(len(grid)):
            if grid[i][0] == 1:
                _ = dfs(i,0,set())
            if grid[i][len(grid[0])-1] == 1:
                _ = dfs(i,len(grid[0])-1,set())
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res+=dfs(i,j,set())
        return res