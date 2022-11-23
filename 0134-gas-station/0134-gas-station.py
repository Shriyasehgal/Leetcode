class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        j = 0
        currCost = 0
        for i in range(len(gas)):
            currCost+=(gas[i] - cost[i])
            if currCost < 0:
                j = 0
                currCost = 0
            else:
                j+=1
                
                if j == n: return i-n+1
        return -1
            
            