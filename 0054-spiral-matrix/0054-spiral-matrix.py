class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix[0])):
            res.append(matrix[0][i])
        matrix.pop(0)
        if matrix:
            res+=(self.spiralOrder(list(zip(*matrix))[::-1]))
        return res
        
        '''m = len(matrix)
        n = len(matrix[0])
        cell = 0,0
        step = (0,1)
        #Changing the cell we have visited to 101
        res = []
        stepChange = [(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)]
        while len(res) != m*n:
            if matrix[cell[0]][cell[1]] == 101 or (cell[0] == m and cell[1] == n): 
                step = stepChange[step]
            else:
                res.append(cell[0][1])
                cell = (cell[0]+step[0],cell[1]+step[1])
        print(res)'''