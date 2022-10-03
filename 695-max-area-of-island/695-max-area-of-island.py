class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,res):
            nonlocal grid
            grid[i][j] = 0 
            curr_res = 0
            if i > 0 and grid[i-1][j] == 1:
                curr_res+=dfs(i-1,j,res)
            if i < len(grid)-1 and grid[i+1][j] == 1:
                curr_res+=dfs(i+1,j,res)
            if j > 0 and grid[i][j-1] == 1:
                curr_res+=dfs(i,j-1,res)
            if j < len(grid[0])-1 and grid[i][j+1] ==1:
                curr_res+=dfs(i,j+1,res)
            return curr_res+1
        final_res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    final_res = max(final_res,dfs(i,j,0))
        return final_res