class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arrPara = [['()']]
        newPara = set()
        for i in range ( 1, n ):
            for comb in arrPara[-1]:
                for j in range(len(comb)):
                    newPara.add(comb[:j+1] + '()' + comb[j+1:])
            arrPara.append(list(newPara))
            newPara.clear()
        return arrPara[-1]
            
            