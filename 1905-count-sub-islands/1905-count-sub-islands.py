class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            grid2[i][j] = 0
            visited.add((i,j))
            if i > 0 and grid2[i-1][j] == 1:
                dfs(i-1,j)
            if j > 0 and grid2[i][j-1] == 1:
                dfs(i,j-1)
            if i < len(grid1)-1 and grid2[i+1][j] == 1:
                dfs(i+1,j)
            if j < len(grid1[0])-1 and grid2[i][j+1] ==1:
                dfs(i,j+1)
        subIslands = 0
        visited = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    for a,b in visited:
                        if grid1[a][b] == 0:
                            subIslands-=1
                            break
                    visited.clear()
                    subIslands+=1
        return subIslands
                    
            