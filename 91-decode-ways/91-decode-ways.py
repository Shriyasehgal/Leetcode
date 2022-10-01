class Solution:
    def numDecodings(self, s: str, memo = {}) -> int:
        if s in memo: return memo[s]
        if s == '':
            return 1
        if s[0] == '0':
            return 0
        count1 , count2 = 0,0
        count1 = self.numDecodings(s[1:],memo)
        if len(s) >= 2 and int(s[0:2]) <=26:
            count2 = self.numDecodings(s[2:],memo)
        memo[s] = count1 + count2
        return memo[s]        