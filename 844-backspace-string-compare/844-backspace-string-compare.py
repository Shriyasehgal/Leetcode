class Solution:
    def result(self,s):
        res =''
        for char in s:
            if char == '#':
                if res:
                    res = res[:-1]
            else:
                res+=char
        return res
                
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.result(s)
        t = self.result(t)
        print(s)
        print(t)
        return s == t