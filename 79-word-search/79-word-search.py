class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i,j,k,visited):
            if (i,j) in visited:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            visited.add((i,j))
        
            if i > 0 and helper(i-1,j,k+1,visited):
                return True
            if i < len(board)-1 and helper(i+1,j,k+1,visited):
                return True
            if j > 0 and helper(i,j-1,k+1,visited):
                return True
            if j < len(board[0])-1 and helper(i,j+1,k+1,visited):
                return True
            visited.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,0,set()):
                    return True
        return False
            
        