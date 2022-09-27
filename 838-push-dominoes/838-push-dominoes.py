class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        new_dominoes = list(dominoes)
        old_dominoes = []
        #Each while loop is i unit of time
        while old_dominoes != new_dominoes:
            old_dominoes = new_dominoes[:]
            for i in range(len(new_dominoes)):
                if old_dominoes[i] == '.':
                    if i > 0 and old_dominoes[i-1] == 'R' and i < len(new_dominoes)-1 and old_dominoes[i+1] == 'L':
                        continue
                    elif  i > 0 and old_dominoes[i-1] == 'R':
                        new_dominoes[i] = 'R'
                    elif  i < len(new_dominoes)-1 and old_dominoes[i+1] == 'L':
                        new_dominoes[i] = 'L'
        return ''.join(new_dominoes)