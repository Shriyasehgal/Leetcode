class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = False
        atl = False
        def dfs(i,j,visited):
            nonlocal pac,atl
            
            if (i,j) in visited:
                return 
            visited.add((i,j))
            if i == 0 or j == 0:
                pac = True
            if i == len(heights)-1 or j == len(heights[0])-1:
                atl = True
            if i > 0 and heights[i][j] >= heights[i-1][j]:
                dfs(i-1,j,visited)
            if i < len(heights)-1 and heights[i][j] >= heights[i+1][j]:
                dfs(i+1,j,visited)
            if j > 0 and heights[i][j] >= heights[i][j-1]:
                dfs(i,j-1,visited)
            if j < len(heights[0]) -1 and heights[i][j] >= heights[i][j+1]:
                dfs(i,j+1,visited)
                
        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                pac = False
                atl = False
                dfs(i,j,visited=set())
                if pac == True and atl == True:
                    res.append([i,j])
        return res
                
            