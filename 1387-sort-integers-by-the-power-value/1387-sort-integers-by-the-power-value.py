class Solution:
    def __init__(self):
        self.memo = {}
    def findPower(self, num):
        if num in self.memo: return self.memo[num]
        if num == 1:
            return 0
        if num%2:
            res = 1 + self.findPower(3*num+1)
        else:
            res = 1 + self.findPower(num/2)
        self.memo[num] = res
        return self.memo[num]
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = []
        for i in range(lo,hi+1):
            power = self.findPower(i)
            powers.append((power, i))
        powers.sort()
        return powers[k-1][1]
        