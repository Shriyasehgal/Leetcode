class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        s = list(s)
        t = list(t)
        while t:
            if s and s[-1] == t[-1]: 
                s.pop()
            t.pop()
        return not s
            
            