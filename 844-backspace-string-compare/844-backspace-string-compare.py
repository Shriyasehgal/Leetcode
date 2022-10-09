class Solution:
    def result(self,s):
        res =''
        stack = []
        for i in range(len(s)-1,-1,-1):
            if s[i] == '#': stack.append('#')
            else:
                if stack:
                    stack.pop()
                else:
                    res= s[i] + res
        return res                
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.result(s)
        t = self.result(t)
        return s == t