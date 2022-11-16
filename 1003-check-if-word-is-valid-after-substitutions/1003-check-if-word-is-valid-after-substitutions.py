class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        t = ''
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 3 and stack[-3:] == ['a','b','c']:
                for i in range(3): stack.pop()
            
        return not stack
