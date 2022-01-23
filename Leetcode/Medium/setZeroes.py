class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        def zeros(i,j):
            for k in range(m):
                if matrix[i][k] != 0:
                    matrix[i][k] = '#'
                    
            for k in range(n):
                if matrix[k][j] !=0:
                    matrix[k][j] = '#'
                    
                
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][j] = '#'
                    zeros(i,j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='#':
                    matrix[i][j] = 0
          
        
