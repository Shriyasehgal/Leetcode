class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        def dfs(i, j, curr):
            if (i,j) in visited: 
                return
            visited.add((i,j))
            image[i][j] = color
            if i > 0 and image[i-1][j] == curr:
                dfs(i-1,j,curr)
            if i < len(image)-1 and image[i+1][j] == curr:
                dfs(i+1,j,curr)
            if j > 0 and image[i][j-1] == curr:
                dfs(i,j-1,curr)
            if j < len(image[0])-1 and image[i][j+1] == curr:
                dfs(i,j+1,curr)
                
        dfs(sr,sc,image[sr][sc])
        return image
                
                
            