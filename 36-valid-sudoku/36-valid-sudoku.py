from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                #checking the value in the  rows:
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                #Checking the value in the col:
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                #Checking the value in the box:
                if board[i][j] in boxs[(j//3)+(i//3)*3]:
                    print(i,j)
                    return False
                boxs[(j//3)+(i//3)*3].add(board[i][j])
        return True