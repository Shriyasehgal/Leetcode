class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0
        j = 0
        currSat = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])
        maxxSat = currSat
        while j <= len(customers)-1:
            while j <= len(customers)-1 and j - i + 1 <= minutes:
                if grumpy[j] == 1:
                    currSat += customers[j]
                    maxxSat = max(maxxSat, currSat)
                j+=1
            if grumpy[i] == 1:
                currSat -= customers[i]
            i+=1
        return maxxSat
            
                    