'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        s_dict={}
        for j in range(1,10):
            for i, sublist in enumerate(board):
                            
                if str(j) in sublist:                 
                  
                    row = [ a for a in range(len(sublist)) if sublist[a] == str(j) ]
                    if len(row)>1:
                        return False
                    val=int((i/3) + (row[0])/3)
                    if 6>i>=3:
                        val=val+2
                    if i>=6:
                        val=val+4
                    if str(j) not in s_dict.keys():
                        s_dict[str(j)]=[]
                    s_dict[str(j)].append((i,sublist.index(str(j)),val))
        
        
        
       
        #For rows and coloumns and subboxes:
        for key in s_dict.keys():
            
            if len(zip(*s_dict[key])[1])!=len(set(zip(*s_dict[key])[1])):
                return False
            if len(zip(*s_dict[key])[2])!=len(set(zip(*s_dict[key])[2])):
                return False
            
           
        return True         
