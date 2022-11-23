class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in rowSet[i]: return False
                    rowSet[i].add(board[i][j])
                    if board[i][j] in colSet[j]: return False
                    colSet[j].add(board[i][j])
                    if board[i][j] in boxSet[(i//3,j//3)]: return False
                    boxSet[(i//3,j//3)].add(board[i][j])
        return True