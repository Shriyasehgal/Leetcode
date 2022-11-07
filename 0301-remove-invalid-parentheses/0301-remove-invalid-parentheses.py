class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0, stack
    
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        visited = set()
        def dfs(s,openPara, closePara):
            visited.add(s)
            if openPara == 0 and closePara == 0 and self.isValid(s)[0] == True: 
                res.append(s)
            for i,c in enumerate(s):
                if c != ')'  and c != '(': continue
                if openPara == 0 and c == '(': continue
                if closePara == 0 and c == ')': continue
                newS = s[0:i] + s[i+1:]
                if newS not in visited:
                    dfs(newS, openPara - (c=='('), closePara - (c==')'))
        
        
        
        stack = self.isValid(s)[1]
        
        openPara = sum([1 for c in stack if c == '('])
        closePara = sum([1 for c in stack if c == ')'])
        dfs(s,openPara, closePara)
        return res
        
        
        