class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = []
        for i, t in enumerate(transactions):
            t = t.split(',')
            trans.append(t)
        res = set()
        trans = list(zip(*trans))
        for i in range(0,len(transactions)):
            if int(trans[2][i]) > 1000:
                res.add(i)
            for j in range(0,i):
                if trans[0][i] == trans[0][j]: 
                    if abs(int(trans[1][i]) - int(trans[1][j])) <= 60 and trans[3][i] != trans[3][j]:
                        res.add(i)
                        res.add(j)
        return [transactions[i] for i in res]
        