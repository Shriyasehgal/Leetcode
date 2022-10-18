class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return '1'
        val = self.countAndSay(n-1)
        i = 0
        j = 0
        res = ''
        while j < len(val):
            curr = ''
            currCount = 0
            while j < len(val) and val[i] == val[j]:
                currCount += 1
                j+=1
            curr += val[i]
            res += str(currCount) + curr
            i = j

        return res