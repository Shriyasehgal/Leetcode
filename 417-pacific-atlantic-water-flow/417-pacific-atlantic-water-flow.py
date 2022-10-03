class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pac,atl = set(),set()
        
        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            if i > 0 and heights[i][j] <= heights[i-1][j]:
                dfs(i-1,j,visited)
            if i < len(heights)-1 and heights[i][j] <= heights[i+1][j]:
                dfs(i+1,j,visited)
            if j > 0 and heights[i][j] <= heights[i][j-1]:
                dfs(i,j-1,visited)
            if j < len(heights[0])-1 and heights[i][j] <= heights[i][j+1]:
                dfs(i,j+1,visited)
                
        for i in range(rows):
            dfs(i,0,pac)
            dfs(i,cols-1,atl)
        for j in range(cols):
            dfs(0,j,pac)
            dfs(rows-1,j,atl)
        return list(pac&atl)
            
                
            