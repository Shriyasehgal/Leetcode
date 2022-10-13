class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sortedCost = []
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        nA = nB = len(costs)//2
        summ = 0
        visited = set()
        for i in range(len(costs)):
            if nA!=0 and nB!=0:

                if costs[i][0] < costs[i][1]:
                    summ += costs[i][0]
                    nA -=1
                else:
                    summ += costs[i][1]
                    nB -=1
            elif nA!=0:
                summ += costs[i][0]
                nA -=1
            else:
                summ += costs[i][1]
                nB -=1

        return summ
            
        
            
        
        '''sortedCost = []
        for i in range(len(costs)):
            sortedCost.append((costs[i][0],i,0))
            sortedCost.append((costs[i][1],i,1))
        sortedCost.sort()
        visited = set()
        visitedA = []
        visitedB = []
        nA = nB = len(costs)//2
        summ = 0
        for cost, i, city in sortedCost:
            if i in visited: continue
            if city == 0:
                if nA == 0: continue
                summ += cost
                visited.add(i)
                nA-=1
                visitedA.append(cost)
            elif city == 1:
                if nB == 0: continue
                summ += cost
                visited.add(i)
                visitedB.append(cost)
                nB-=1
            
        print(visitedA)
        print(visitedB)
        return summ'''
                
            
                
                
                
            
            