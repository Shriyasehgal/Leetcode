class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        t = -3
        for c in s:
            stack.append(c)
            t+=1
            if t >= 0 and stack[t:] == ['a','b','c']:
                stack.pop()
                stack.pop()
                stack.pop()
                t = t-3
            
        return not stack
            
            