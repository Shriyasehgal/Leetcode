class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if  obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '#'
        for i in range(m):
            if obstacleGrid[i][0]!='#':
                obstacleGrid[i][0] = 1
                break
        for j in range(n):
            if obstacleGrid[0][j] != '#':
                obstacleGrid[0][j] = 1
                break

        for i in range(0,m):
            for j in range(0,n):

                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i][j] == '#':
                    obstacleGrid[i][j] = 0
                else:
                    left_val = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != '#' else 0
                    right_val = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != '#' else 0
                    obstacleGrid[i][j] = left_val + right_val
        
        return obstacleGrid[-1][-1]
                    
                    
        
