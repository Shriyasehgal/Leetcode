class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curr = 0
        
        for i,(g,c) in enumerate(zip(gas*2,cost*2)):
            if i - start == len(gas):
                return start
            curr = curr + g - c
            if curr < 0:
                curr = 0
                start = i+1
        return -1