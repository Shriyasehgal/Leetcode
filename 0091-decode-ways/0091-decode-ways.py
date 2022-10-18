class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if s == '': return 1
        res = 0
        if len(s) > 1 and int(s[0:2]) <= 26 and int(s[0:2]) >= 10:
            res += self.numDecodings(s[2:])
        if int(s[0]) >= 1 and int(s[0]) <= 9:
            res += self.numDecodings(s[1:])
        return res
        
        