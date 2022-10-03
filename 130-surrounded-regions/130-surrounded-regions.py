class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i,j, visited):
            if board[i][j] == 'X':
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            board[i][j] = '#'
            
            if i > 0 and board[i-1][j] == 'O':
                dfs(i-1,j,visited)
            if i < len(board)-1 and board[i+1][j] == 'O':
                dfs(i+1,j,visited)
            if j > 0 and board[i][j-1] == 'O':
                dfs(i,j-1,visited)
            if j < len(board[0]) - 1 and board[i][j+1] == 'O':
                dfs(i,j+1,visited)
        
        for i in range(rows):
            dfs(i,0,set())
            dfs(i,cols-1,set())
            
        for j in range(cols):
            dfs(0,j,set())
            dfs(rows-1,j,set())
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
                

            